---
name: vlsit-vhdl-to-systemverilog
description: Convert complete VHDL RTL designs into readable, synthesizable SystemVerilog under the bundled VLSIT coding rules. Analyze semantics and rule conflicts, obtain plan sign-off, preserve cycle behavior, and deliver source mappings, rule evidence, and actual validation results.
---

# VHDL to SystemVerilog

## Language convention

Use precise scientific and engineering English for skill instructions, technical clarifications, review gates, plans, reports, RTL comments, diagram labels, manifests, and script messages. Use consistent terminology and distinguish observed results from assumptions. Bilingual English–Vietnamese content is reserved for README files and documents explicitly designated as user guidelines.

Convert the supplied design RTL and its dependencies while preserving the approved hardware behavior. Write RTL identifiers and functional comments in English under the rule file.

## Mandatory rules

- Before analyzing or generating RTL, read the entire [VLSIT_RTL_Design_Rule.md](references/VLSIT_RTL_Design_Rule.md), including tables, nested requirements, file structure, and the tapeout checklist. It is the authoritative, separately maintained rule file inside this skill; do not substitute a summary or depend on an external machine path.
- Apply every applicable requirement to every generated design module. Follow MUST/MUST NOT without waivers. Follow SHOULD by default; only deviations explicitly permitted by the rule file may have a documented reason. N/A requires proof that the feature is absent or the condition is inapplicable; missing tools or evidence is NOT_RUN, never N/A or PASS.
- Do not weaken or edit the rule file to make a conversion pass. If source behavior and a mandatory rule conflict, document the conflict and ask for a compliant resolution. User approval of a behavior change does not make it an equivalent translation; label that portion as redesign. An unresolved conflict blocks a compliant handoff.

## Inputs

- Require an explicit VHDL source directory. If absent or ambiguous, ask for it before inspecting RTL; do not infer it from the workspace or a previous design. The bundled rule is already supplied and must not be requested again.
- Discover tops, entity/architecture bindings, library dependencies, file order, VHDL standard, generics, existing testbenches, and constraints. Ask about unresolved choices that affect behavior, supported configurations, external names, or validation. Specification and testbench inputs are optional; missing specification means the source is the behavioral baseline, not permission to invent requirements.
- Confirm output directory, synthesis target/frontend/version, required validation level, project name, and human author before final generation. If output is unspecified, propose a new vhdl_to_sv_output directory under the source project for Gate 1. Never overwrite input RTL, existing output, or user changes; use a new directory for each run.

## 1. Baseline and plan

Read [vhdl_semantics.md](references/vhdl_semantics.md) before planning each conversion. Inventory every source file and design unit, including unused units in the chosen RTL source set. Classify each as converted, absorbed dependency, verification-only, explicitly excluded by the user, or blocked. Unresolved bindings and vendor primitives cannot disappear into empty stubs. Record source hashes, selected architectures, all supported generic configurations, clocks/resets, external protocol contracts, and known source defects.

Create conversion_plan.md with findings in scientific English and source evidence: scope, baseline behavior, source-to-target mappings, semantic risks, per-rule conflicts, proposed hierarchy/port changes, tool availability, exact validation configurations, and open questions. Use [validation_and_reports.md](references/validation_and_reports.md). Generate the initial rule evidence matrix using scripts/create_rule_matrix.py; read the original rule to expand every compound requirement into subchecks.

**Gate 1:** Present the concrete plan/version and ask the user to approve, revise, or stop. Wait for approval before creating converted RTL. Approval already given for that exact plan remains valid. Reopen only decisions whose behavior or scope changes. Report creation and read-only source/tool analysis are allowed before this gate.

## 2. Convert

- Translate from understood behavior, not textual substitutions. Preserve cycle latency, priority, widths, overflow, bit order, memory semantics, handshakes, interrupts, and reset behavior within the approved equivalence contract. Split sequential and combinational logic without changing same-cycle variable dependencies or next-cycle signal updates.
- Follow the full bundled rule: IEEE 1800-2017 within frontend support, unsigned logic datapaths, explicit widths, local types, named connections, structural top, one module per matching .sv filename, approved reset/CDC/DFT structures, required names/comments/headers, and every prohibited-construct restriction. These examples do not replace the complete rule checklist.
- Preserve license and attribution alongside the required VLSIT header. Do not silently repair source bugs, change FSM encoding, add resets or pipeline stages, add scan ports, or restrict generic values. Explain and approve any necessary redesign separately; preserve a mapping for integration and verification.
- Use automation only where its transformation is understood. GHDL-generated Verilog may be an intermediate reference; it is not automatically readable, rule-compliant SystemVerilog or an independent proof of equivalence. Preserve the independently elaborated VHDL baseline.

## 3. Validate and deliver

Follow [validation_and_reports.md](references/validation_and_reports.md). Run available checks authorized by the approved plan, inspect logs, and fix candidate defects without changing the baseline. Check source and target configurations, lint and semantic rule evidence, differential simulation, formal equivalence when supported, synthesis/inference, and applicable CDC/RDC/DFT requirements. Missing tools must be reported; they never justify success claims.

Deliver rtl/, filelists/, verification/, logs/, conversion_plan.md, conversion_manifest.json, rule_compliance.json, and conversion_report.md. Use relative paths and user-supplied runtime roots rather than embedding laptop paths in reusable files. Reports must distinguish conversion completeness, rule compliance, synthesis results, equivalence evidence, and tapeout readiness. Line-change percentage cannot demonstrate conversion correctness.

**Gate 2:** Present actual evidence and remaining limitations for user review. User acceptance cannot change NOT_RUN/FAIL into PASS. Only label the result accepted within the documented scope when the user accepts it and all required planned checks and applicable mandatory rules pass. Simulation matching alone is not a formal proof; approved redesign is not unchanged equivalence.
