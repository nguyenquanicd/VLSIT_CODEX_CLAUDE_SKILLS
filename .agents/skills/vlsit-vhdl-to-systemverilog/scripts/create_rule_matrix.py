#!/usr/bin/env python3
"""Create an unassessed evidence matrix from the bundled VLSIT rule document.

This is a document inventory helper, not a semantic RTL compliance checker.
Uses only the Python standard library; never overwrites an existing output.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path


def collect_entries(text):
    """Collect explicit rules plus non-code table/list/naming requirements."""
    lines = text.splitlines()
    entries = []
    official_ids = set()
    auxiliary_count = 0
    headings = {}
    fence_marker = None
    fence_length = 0
    marker_pattern = r'^\s*(' + chr(96) + r'{3,}|~{3,})(.*)$'

    for index, line in enumerate(lines):
        fence = re.match(marker_pattern, line)
        if fence:
            marker, suffix = fence.groups()
            if fence_marker is None:
                fence_marker, fence_length = marker[0], len(marker)
            elif (
                marker[0] == fence_marker
                and len(marker) >= fence_length
                and not suffix.strip()
            ):
                fence_marker = None
            continue
        if fence_marker is not None:
            continue

        heading = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading:
            level = len(heading.group(1))
            headings = {k: v for k, v in headings.items() if k < level}
            headings[level] = heading.group(2).strip()
            continue

        identifier = None
        kind = None
        requirement = None
        official = re.match(r'^-\s+\*\*([A-Z]+-\d+)\*\*\s*(.*)$', line)
        prohibition = re.match(r'^\|\s*(P\d+)\s*\|(.+)\|\s*$', line)
        if official:
            identifier, requirement = official.groups()
            kind = 'numbered_rule'
        elif prohibition:
            identifier = prohibition.group(1)
            requirement = line.strip()
            kind = 'prohibition'
        elif line.lstrip().startswith('|') and line.rstrip().endswith('|'):
            # Skip table headers and separator rows, preserving each data row.
            separator = r'[\s|:\-]+'
            next_line = lines[index + 1] if index + 1 < len(lines) else ''
            if re.fullmatch(separator, line) or re.fullmatch(separator, next_line):
                continue
            kind, requirement = 'table_requirement', line.strip()
        elif re.match(r'^-\s+', line):
            kind, requirement = 'unnumbered_item', line[2:].strip()
        elif re.match(r'^\d+[.)]\s+', line):
            kind, requirement = 'structure_step', line.strip()
        elif line.startswith(('Use lowercase snake_case', 'Keep in full, never abbreviate:')):
            kind, requirement = 'naming_instruction', line.strip()

        if kind is None:
            continue
        if identifier is not None:
            if identifier in official_ids:
                raise ValueError(f'Duplicate rule identifier: {identifier}')
            official_ids.add(identifier)
        else:
            auxiliary_count += 1
            identifier = f'AUX-{auxiliary_count:04d}'
        entries.append({
            'id': identifier,
            'kind': kind,
            'section': ' / '.join(headings[k] for k in sorted(headings)),
            'source_line': index + 1,
            'requirement': requirement,
            'status': 'NOT_RUN',
            'scope': [],
            'subchecks': [],
            'evidence': '',
            'reason': '',
            'reviewer': '',
        })

    if not entries:
        raise ValueError('No rule entries found; inspect the bundled document.')
    if fence_marker is not None:
        raise ValueError('Unclosed code fence in the rule document.')
    return entries


def build_matrix(rule_path):
    raw = rule_path.read_bytes()
    text = raw.decode('utf-8-sig')
    return {
        'format_version': 2,
        'rule_document': 'references/VLSIT_RTL_Design_Rule.md',
        'rule_sha256': hashlib.sha256(raw).hexdigest().upper(),
        'assessment': 'NOT_RUN',
        'notes': [
            'Document inventory only; this script does not examine or certify RTL.',
            'Read the complete rule and expand compound requirements into subchecks.',
            'AUX identifiers are helper labels, not official VLSIT rule identifiers.',
            'Evidence and applicability must cover every generated design module and configuration.',
        ],
        'entries': collect_entries(text),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='New JSON evidence file.')
    args = parser.parse_args()
    rule_path = (
        Path(__file__).resolve().parent.parent
        / 'references'
        / 'VLSIT_RTL_Design_Rule.md'
    )
    try:
        matrix = build_matrix(rule_path)
        payload = json.dumps(matrix, ensure_ascii=False, indent=2) + '\n'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8', newline='\n') as stream:
            stream.write(payload)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f'Cannot create matrix: {error}\n')
    count = len(matrix['entries'])
    digest = matrix['rule_sha256']
    print(f'Created {count} NOT_RUN entries. Rule SHA-256: {digest}')


if __name__ == '__main__':
    main()
