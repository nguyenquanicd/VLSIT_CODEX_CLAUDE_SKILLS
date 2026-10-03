---
name: opencore-ip-downloader
description: Search OpenCores and its linked public repositories for open-source hardware IP, then download each project with its RTL, documentation, license, and related collateral. Use when asked to find and collect existing IP cores; not for designing a new core.
---

# OpenCores IP Search and Download

Find existing open-source hardware IP that matches the user's description, then collect the complete available project package for each selected IP. OpenCores is the primary catalog; use its official download or linked upstream repository where possible.

## Required information

Before starting downloads, make sure the request establishes all three:

1. The IP type and a short description of the intended function, standard, or use case.
2. How many distinct open-source IP implementations the user wants.
3. The absolute folder where the files should be saved.

Ask for all missing details together, in the user's language, then wait for the answer before downloading. Do not infer a download destination from the current directory, this skill's location, or an unrelated earlier task. If the user supplies a minimum count, treat it as the target and report when fewer suitable projects exist; never invent projects or count duplicate mirrors as separate IPs.

## Find and select projects

1. Search the OpenCores projects catalog for the described function and relevant aliases, standards, interfaces, and terms.
2. Open candidate project pages and follow their official download links. If a project points to a public upstream repository or mirror, use that repository when it contains the complete project or is the only working source. Search other public open-source repositories only when needed to find more distinct candidates; label those results as external to OpenCores.
3. Confirm that each candidate implements the requested function from its project description and available source or documentation. Prefer distinct, synthesizable RTL projects with useful documentation, test collateral, and a clear license. Do not count forks, mirrors, or repackagings of the same upstream project as separate implementations.
4. Include a project in the open-source count only when its RTL/source is publicly available under a clearly identified open-source license. Preserve the license text and link. If licensing is missing or unclear, do not claim that project is open source or include it in the confirmed count; you may report it separately as an unconfirmed candidate. Exclude proprietary or access-restricted material.

## Download complete project materials

For every selected IP, download the full project archive or repository snapshot, not only a few RTL files. Preserve the upstream directory structure and include all project materials that are available, such as:

- RTL/HDL source, packages, wrappers, and project or file lists
- README files, specifications, user guides, manuals, and other project documentation
- License and copyright notices
- Testbenches, test vectors, simulation or formal collateral
- Synthesis/build scripts, constraints, example designs, and software drivers or examples
- Project metadata and declared submodules or dependencies needed to use the project, when publicly available

Follow only links that are part of the selected project's distribution. Do not treat unrelated site pages, external references, or an entire hosting account as project collateral. Do not execute downloaded code. Do not run simulation, lint, synthesis, or other tests unless the user asks for them.

## Save and record provenance

- Create a separate, clearly named subfolder for each distinct project inside the user-selected destination. Check for existing files first; never silently overwrite user data. If a name collides, choose a new descriptive folder name or ask the user when the conflict cannot be resolved safely.
- Keep the original archive when practical, alongside its extracted project tree. For a repository snapshot, record its exact revision or commit when available.
- Add a concise DOWNLOAD_INFO.md in each project folder with the project name, catalog/upstream URLs, download date, revision or archive name, license and license URL, SHA-256 of the downloaded archive when available, and any unavailable or excluded project materials.
- Add or update a destination-level CATALOG.md listing the selected projects, their source, license, and a brief description. Preserve any existing catalog content and do not overwrite unrelated files.

## Check the collection

Confirm each download completed and that archives can be listed or pass their built-in archive integrity check before extraction. Inspect archive paths for unsafe traversal before extracting. Record the downloaded file's SHA-256 when practical. Check that the extracted project contains the expected source and the documentation/license files advertised by the project; report omissions accurately. These are download-integrity checks, not claims that the RTL was simulated or validated.

## Report back

Summarize the requested count, how many distinct licensed projects were found and downloaded, and the destination folder. For each project, give its name, source link, license, and the main materials collected. Identify external-to-OpenCores results, missing collateral, unclear licenses, or failed downloads. Do not claim that RTL works, synthesizes, or passes tests unless that work was separately requested and performed.
