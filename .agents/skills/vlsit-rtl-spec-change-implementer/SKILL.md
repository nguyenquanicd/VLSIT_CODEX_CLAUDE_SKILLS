---
name: vlsit-rtl-spec-change-implementer
description: Analyze existing RTL against an optional prior specification and a requested new feature, present a minimal-change plan in scientific English for explicit user sign-off, then implement only the approved changes and report the RTL code-change percentage.
---

# RTL Specification Change Analysis and Implementation

## Language convention

Use precise scientific and engineering English for skill instructions, technical clarifications, review gates, plans, reports, RTL comments, diagram labels, manifests, and script messages. Use consistent terminology and distinguish observed results from assumptions. Bilingual English–Vietnamese content is reserved for README files and documents explicitly designated as user guidelines.

Use this skill when a user wants an existing RTL design analyzed against an earlier specification and a new feature or behavior requirement, then minimally updated after review.

## Inputs and clarification

- A specific existing RTL source directory is mandatory. Do not infer it from the current workspace, repository root, a prior task, or a specification path. If it is missing or ambiguous, ask for the RTL directory before inspecting RTL.
- An old/original specification is optional. If supplied, use it to identify existing requirements and detect conflicts or regressions. If absent, derive the baseline behavior from RTL and clearly state that comparison against a written old specification was unavailable.
- A new specification file is optional only when the user describes the requested new behavior in the prompt or supplies that description in response to clarification. If neither is present, ask for the new specification path or ask the user to describe the requested feature/change in the same reply.
- Ask only for missing or materially ambiguous information. Bundle missing inputs into one concise technical question when practical. Example:
  - Please provide (1) the RTL source directory (required), (2) the old specification path or “none” (optional), and (3) the new specification path, or describe the requested feature if no new spec file exists.
- If a new spec and the user's prose differ, identify the difference and ask which is authoritative before planning affected behavior.
- Clarify ambiguities that materially affect interface, timing, reset, register behavior, compatibility, or externally visible behavior. Do useful read-only analysis while awaiting answers, but do not guess these decisions.

## Workflow and approval gate

### 1. Establish the baseline

- Inspect the supplied RTL tree and relevant local context: module hierarchy, interfaces, parameters, existing behavior, coding conventions, file lists, and existing verification instructions. Inspect old/new specifications and map each new requirement to relevant RTL modules/files.
- Separate what the source proves from interpretation. Record gaps, contradictions, conditional behavior, unresolved modules, and existing working-tree changes that could affect a clean comparison.
- Do not run tests, simulations, synthesis, or other executable checks during analysis. Do not edit RTL during this phase.
- Preserve the user's existing changes. Never treat an unrelated prior snapshot or repository output folder as the current baseline.

### 2. Prepare a detailed change plan

Before editing any RTL, prepare a review document in scientific English named rtl_change_review.md. Save it to a user-specified output location; otherwise use the project root containing the supplied RTL directory when identifiable. If the location is ambiguous or not writable, ask where to save it. Do not silently overwrite an existing report; choose a numbered filename or ask.

The plan must include:

1. Design and input summary: RTL root, old spec status, new spec source, selected top/modules, and analysis limits.
2. Requirement comparison: each new requirement, relevant old requirement or “not supplied,” current RTL behavior with source evidence, and intended behavior.
3. Affected-module/file map: exact module, file, relevant code region, proposed change, and why it is needed.
4. Design choices: present no more than three strong implementation strategies, and only when there are materially different viable options. Rank them, recommend one, and compare functional coverage, change size, interface/backward compatibility, complexity, and risk. If only one sound approach exists, present one.
5. Minimal-change rationale: explain why each planned edit is necessary; identify related code explicitly excluded from the change.
6. Open questions, assumptions, conflicts, and compatibility risks.
7. Proposed validation: specific existing checks that could verify the change, their commands when discoverable, and expected evidence. Do not claim a check has run.
8. A clear approval status, such as “Awaiting user sign-off.”

Write the review document in scientific English. Use precise requirement terminology and make each finding, rationale, and table row independently understandable.

Then summarize the proposed plan in chat in scientific English and ask the user to approve, revise, or stop. Approval must refer to the presented plan/version and exact scope. The initial request to add a feature is not approval of an unseen implementation plan.

- Until explicit approval, do not modify RTL, create patches in source files, run checks, or make unrelated project edits. Preparing and revising the review document is allowed.
- If the user requests revisions, update the plan and present the revised version for sign-off. Wait for the user's response before implementation.
- If the user stops or does not approve, make no RTL changes; leave the review document marked as not approved.
- Treat approval as limited to the listed files, behaviors, strategy, and checks. If implementation reveals a necessary change outside the approved scope, stop, update the plan, and request approval for the expanded scope before proceeding.

Approval prompt:
- Do you approve plan version N, including the listed RTL files, proposed behavior, and validation commands? Reply APPROVE, REVISE, or STOP.

### 3. Implement only the approved change

- Make the smallest safe set of RTL changes that fully implements the approved behavior. Prefer existing architecture, naming, reset, handshake, register, and coding patterns. Avoid unrelated cleanup, redesign, renaming, formatting churn, or broad refactoring.
- Minimality must not compromise correctness, timing/interface contracts, reset behavior, parameterized configurations, or maintainability. If a tiny patch would be fragile or incomplete, use the smallest robust approach and explain why.
- Do not invent unspecified behavior. Follow approved decisions and assumptions. If new evidence changes the planned solution, return to the approval gate.
- Modify only approved RTL files and any explicitly approved supporting files. Do not edit either specification unless separately requested.
- Preserve the RTL source language and existing comment style. Write new functional comments, plans, and reports in scientific English.

### 4. Validate and report

- Run only the validation commands explicitly listed and approved in the plan or separately requested by the user. Do not add tests or claim lint, compile, simulation, synthesis, or formal success unless that exact check was run and its result inspected.
- Compare final RTL to the task-start baseline, not blindly to HEAD if the working tree was already dirty. Isolate this task's edits from pre-existing user changes.
- Update rtl_change_review.md with the final implementation report. Include requirement-to-code traceability; changed files and concise per-file summary; actual checks and results; remaining risks or unimplemented items; and a clear completion status.
- Report the RTL code-change percentage with raw counts and scope:
  - Baseline denominator: count nonblank, non-comment RTL code lines across the supplied RTL source tree before this task's edits.
  - Change numerator: task-specific nonblank, non-comment RTL lines added plus such lines deleted, measured against the captured task-start baseline. A replaced line counts once as deleted and once as added.
  - Percentage: (added RTL code lines + deleted RTL code lines) / baseline RTL code lines × 100.
  - State total baseline RTL code lines, added lines, deleted lines, changed-file list, and percentage. The ratio can exceed 100% if the change adds more code than the original design size.
  - Exclude Markdown reports, comments-only changes, blank lines, generated logs, tests, and unrelated/pre-existing edits from the numerator. The denominator covers the supplied RTL tree, not only edited files.
  - Use a captured content snapshot or equivalent diff against the task-start files if version control cannot isolate the baseline. If an exact task-specific comparison is impossible, report the percentage as unavailable and explain why; never estimate or fabricate it.
- Write the final report and technical response in scientific English. Clearly distinguish verified results, source-based reasoning, assumptions, and validation limitations.

## Final response

Provide the review/report file link and a concise technical summary in scientific English of approved behavior, RTL files changed, implementation status, RTL code-change percentage with formula counts, executed checks and results, and outstanding risks.
