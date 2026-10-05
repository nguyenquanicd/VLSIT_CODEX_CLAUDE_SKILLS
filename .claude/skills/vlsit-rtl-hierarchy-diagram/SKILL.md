---
name: vlsit-rtl-hierarchy-diagram
description: Analyze existing Verilog or SystemVerilog RTL to trace module hierarchy, functional relationships, and protocol interfaces, then create a source-grounded multi-page draw.io diagram using only the bundled VLSIT symbol library. Use when asked to inspect or map a design from its top module to its submodules.
---

# VLSIT RTL Hierarchy Analysis and draw.io Diagram

## Language convention

Use precise scientific and engineering English for skill instructions, technical clarifications, review gates, plans, reports, RTL comments, diagram labels, manifests, and script messages. Use consistent terminology and distinguish observed results from assumptions. Bilingual English–Vietnamese content is reserved for README files and documents explicitly designated as user guidelines.

Analyze the existing RTL source and create an editable diagrams.net `.drawio` file. Do not modify RTL source files.

## Mandatory symbol library

- Use only [assets/VLSIT_DRAWIO_LIB_V1.drawio.xml](assets/VLSIT_DRAWIO_LIB_V1.drawio.xml) as the source of every visible block, logic symbol, connector, text annotation, and note-panel shape. Read [references/library_usage.md](references/library_usage.md) before generation. The library is part of this skill and must be copied with it during installation.
- Parse the library and inspect the selected templates. Clone their complete cell structures, remap identifiers and internal references, and retain template provenance on each cell as specified in the reference. Use entry 32 for module blocks and bordered panels, entry 0 for standalone text, and entry 27 or another supplied connector template for links.
- Preserve template shape definitions, gate operations, arrowheads, and group topology. Adapt labels, placement, dimensions, and permitted presentation properties to meet the visual requirements below. Do not import other libraries, choose unrelated built-in symbols, insert images, or invent substitute shapes.
- Library placeholders describe templates, not the RTL. Replace them with source-grounded content and use logic symbols only when the requested detail and actual RTL justify them. If a required symbol is absent, ask for an extension to this library or an agreed representation using its existing templates; do not silently fall back to another symbol source.
- If the bundled asset is missing, unreadable, or invalid, stop diagram generation and ask for the correct library. Do not substitute a local-machine file or regenerate a purported copy from memory.

## Required input: RTL source directory

- Before locating or reading RTL, require an explicit path to the RTL source directory for the current analysis request. If the user has not provided one, ask: “Please provide the path to the RTL directory you want analyzed.” Then wait; do not search for or analyze RTL until they reply.
- Do not infer the RTL directory from the current working directory, repository root, skill directory, output path, or a path from an unrelated prior task. If the provided path is missing, invalid, or ambiguous between a repository root and the RTL source directory, ask the user to clarify it.
- After receiving a valid path, use it as the RTL source root and then follow the workflow below.

## Workflow

1. Locate RTL files and relevant project context, such as file lists, build scripts, constraints, and configuration. Respect any user-specified source or output path.
2. Identify the top module from the user's instruction or project configuration. If several candidates remain, state them and the assumption used rather than silently choosing one.
3. Trace module instantiations recursively. Record each instance name, module name, source file, hierarchy depth, parent, parameters, and relevant generate scope. Treat packages and interfaces as source context, not module-instance blocks unless instantiated as modules.
4. Trace port connections through parent nets and assignments. Identify important data, control, status, and interrupt paths between instances, including sibling modules connected through their parent. Distinguish actual RTL connections from functional interpretation.
5. Analyze each relevant module's RTL beyond its name and comments. Follow its key state, datapath, control logic, and port behavior to write a concise, source-grounded description of what the block does and how it participates in the design. Describe an instance-specific role only when its connections and surrounding RTL support it; otherwise state the module-level role and mark the instance role as unclear.
6. Identify standard and internal interfaces from the actual port mapping and RTL handshake behavior. Look for APB, AXI read/write channels, valid/ready, request/acknowledge, FIFO push/pop, interrupts, and other recognizable interfaces. Confirm protocol labels from multiple relevant signals and behavior, not from a module or signal name alone. Record direction, endpoints, and the key signals present in this design; omit signals that are absent or not connected.
7. Account for generate blocks and parameters when the source or project configuration makes the active hierarchy clear. If multiple configurations are possible, label conditional branches and explain the uncertainty. Do not invent missing modules, instances, connections, protocol compliance, or behavior; identify unresolved or external modules explicitly.

## draw.io file and page order

- Save an editable, multi-page diagrams.net XML file named `rtl_hierarchy.drawio` in the workspace unless the user specifies another output path. Do not substitute Mermaid, an image, or a PDF for the `.drawio` deliverable.
- Create one page per hierarchy depth in the same file. Depth 0 is the top module. Name pages `00_TOP`, `01_LEVEL_1`, `02_LEVEL_2`, and so on. Order the `<diagram>` pages in the XML in that sequence so the tabs appear left to right from TOP to the deepest level.
- On `00_TOP`, show the top module, its external interface annotations, and its function summary. On each later page, show the modules at that depth, their immediate parent modules from the preceding depth for context, and the parent-to-child instantiation links. A module at an earlier leaf depth need not be repeated on deeper pages.
- Label every module block with exactly two centered lines: put the instance name on line 1 and the module name in parentheses on line 2, for example `u_fifo` on line 1 and `(axis_downscaler_fifo)` on line 2. For the top block, use `TOP` on line 1 unless the user or source provides a more appropriate top instance label, and put `(top_module_name)` on line 2. Keep separate blocks for separate instances, even when they instantiate the same module type.
- Show both structural hierarchy and important functional relationships. Keep parent-to-child instantiation links as thin black arrows. Add distinct, labeled black connectors for important data/control/handshake paths between visible blocks when those paths can be traced through RTL port maps and parent nets. Use line weight or pattern plus a small legend to distinguish functional links from hierarchy links; keep all colors black and white. Do not draw speculative connections or imply a direct connection when RTL shows only a shared parent or an indirect path.
- Annotate functional connectors with the interface name, direction, and concise key-signal group. Examples include `APB` with the connected `PSEL`, `PENABLE`, `PADDR`, `PWRITE`, `PWDATA`, and response signals; `AXI write` with the present `AW*`, `W*`, and `B*` channels; `AXI read` with the present `AR*` and `R*` channels; `valid/ready` or `request/acknowledge` handshakes; and `interrupt`/`IRQ` paths. Include only ports that exist and are actually connected. Do not label an interface as AXI/APB compliant unless the RTL evidence supports that protocol identification.
- Add one clearly bordered `Block Functions & Interfaces` panel to every page. Give a concise, RTL-grounded function description for every visible block and summarize its important interfaces or role in the functional paths. For repeated instances with the same module behavior, group the description by module type but list the instance names it covers; add instance-specific roles when their wiring shows a meaningful difference. Include source file and line references when practical. Keep descriptions concise, but expand the panel or page as needed rather than clipping text or shrinking it below 18 pt.
- Use solid black outlines for modules resolved in source and dashed black outlines for unresolved or external modules. State unresolved items in a small note or the completion summary.

## Visual requirements

- Use black and white only: white page and block fills, black borders, black text, and black connectors. Do not use colored accents, gray fills, gradients, or shadows.
- Set all visible diagram text, including block labels and titles, to 18 pt.
- Size each block around its two-line label: make the width fit the longer line with modest side padding, and the height fit two 18 pt lines with modest top and bottom padding. Let blocks with longer names be wider; keep similarly sized labels in similarly sized blocks. Do not stretch blocks to fill the page or leave large empty margins around short labels. Keep the two-line label intact rather than forcing both names onto one long line or wrapping it into extra lines.
- Place sibling blocks close together with consistent, compact gaps: leave enough room to distinguish adjacent borders and route connectors cleanly, without excessive horizontal or vertical whitespace. Align each hierarchy depth consistently and center parent blocks over their children where practical.
- Place the function panel beside or below the block layout, not inside module blocks. Give it enough width and height for readable descriptions, and expand the page rather than crowding blocks or connectors. Keep the panel's text black on white at 18 pt.
- Route connectors and labels to avoid overlap and unnecessary crossings. Choose page size and orientation to fit both the block layout and function panel with balanced margins, preserving readable spacing without clipping or crowding.

## Deliverables

Provide the `.drawio` file and briefly report the selected top module, page/tab names, RTL files inspected, key functional relationships and identified interfaces, and unresolved or conditional hierarchy. Record the bundled library filename, SHA-256, and template indices used. Check that the XML is well-formed and that block descriptions, interface labels, and connections are consistent with the traced RTL.

Before handoff, run `python scripts/library_symbols.py validate --diagram <GENERATED_DRAWIO_FILE>` from this skill folder. Correct failed provenance, shape, group, or styling checks before claiming library compliance. If the checker cannot run, disclose that limitation and perform an explicit comparison against the bundled templates; do not claim that the automated check passed. The checker does not prove RTL correctness or visual quality.

If a preview can be rendered, inspect it for text fit, clipping, overlap, connector labels, tab order, spacing, and faithful library-symbol appearance; state clearly if visual rendering could not be checked.
