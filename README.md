# Skills for Codex and Claude Code / Bộ skill cho Codex và Claude Code

This repository contains four paired project skills. Every skill has a Codex copy and a Claude Code copy, plus a short bilingual README.

Repository này có bốn skill dự án, mỗi skill gồm bản Codex và Claude Code cùng README song ngữ ngắn.

## Language convention / Quy định ngôn ngữ

Skill instructions, technical references, code comments, plans, reports, diagram labels, and script outputs use precise scientific and engineering English. Only README files and explicitly designated user guidelines use bilingual English–Vietnamese content.

Nội dung skill, tài liệu tham khảo kỹ thuật, comment code, kế hoạch, báo cáo, nhãn sơ đồ và đầu ra script dùng tiếng Anh khoa học và kỹ thuật chuẩn. Chỉ README và tài liệu được xác định rõ là guideline cho người dùng sử dụng song ngữ Anh–Việt.

## Skill locations / Vị trí skill

| Tool | Project-level folder | Personal folder |
|---|---|---|
| Codex | .agents/skills/<skill-name>/ | Current Codex docs: $HOME/.agents/skills/<skill-name>/; some installer setups use $CODEX_HOME/skills/<skill-name>/ |
| Claude Code | .claude/skills/<skill-name>/ | $HOME/.claude/skills/<skill-name>/ |

The project folders are the most portable choice for this repository. Commit them to share the skills with teammates. Read the per-skill README for each skill’s functions and input/output details.

Thư mục project là cách dùng ổn định nhất cho repository này. Commit các thư mục đó để chia sẻ skill với nhóm. Xem README của từng skill để biết chức năng và đầu vào/đầu ra cụ thể.

## Skills / Danh sách skill

| Skill | Purpose / Mục đích | Guides / Hướng dẫn |
|---|---|---|
| opencore-ip-downloader | Find licensed open-source hardware IP with RTL, download complete projects, and compare features and FPGA/ASIC readiness. / Tìm IP phần cứng mã nguồn mở có RTL, tải dự án đầy đủ và so sánh tính năng cùng khả năng FPGA/ASIC. | [Codex](.agents/skills/opencore-ip-downloader/README.md) · [Claude](.claude/skills/opencore-ip-downloader/README.md) |
| rtl-hierarchy-diagram | Trace RTL hierarchy and important interfaces, then create a multi-page Draw.io diagram with module summaries. / Lần theo hierarchy và interface RTL, sau đó tạo sơ đồ Draw.io nhiều trang kèm tóm tắt module. | [Codex](.agents/skills/rtl-hierarchy-diagram/README.md) · [Claude](.claude/skills/rtl-hierarchy-diagram/README.md) |
| vlsit-rtl-spec-change-implementer | Analyze RTL against a new feature and optional old spec, gate implementation behind approval of an English technical plan, and report RTL code-change percentage. / Phân tích RTL theo yêu cầu mới và spec cũ tùy chọn, chờ duyệt kế hoạch kỹ thuật tiếng Anh trước khi triển khai và báo cáo tỷ lệ code RTL thay đổi. | [Codex](.agents/skills/vlsit-rtl-spec-change-implementer/README.md) · [Claude](.claude/skills/vlsit-rtl-spec-change-implementer/README.md) |
| vlsit-vhdl-to-systemverilog | Convert complete VHDL RTL into synthesizable SystemVerilog under the bundled VLSIT rules, with semantic analysis, two review gates, source mappings, and evidence-based validation. / Chuyển đầy đủ RTL VHDL sang SystemVerilog tổng hợp được theo rule VLSIT đi kèm, có phân tích semantics, hai gate duyệt, mapping nguồn và kiểm chứng bằng bằng chứng. | [Codex](.agents/skills/vlsit-vhdl-to-systemverilog/README.md) · [Claude](.claude/skills/vlsit-vhdl-to-systemverilog/README.md) |

The VHDL conversion skill includes its own separately maintained references/VLSIT_RTL_Design_Rule.md. The agent must read the complete rule and assess every applicable requirement. Copy the entire skill folder, including references and scripts. Plan approval precedes conversion; final review distinguishes rule compliance, synthesis, and equivalence results.

Skill chuyển VHDL chứa file references/VLSIT_RTL_Design_Rule.md riêng trong skill. Agent bắt buộc đọc đầy đủ rule và đánh giá mọi yêu cầu phù hợp. Chép toàn bộ thư mục skill, gồm references và scripts. Duyệt kế hoạch trước khi chuyển; duyệt cuối tách kết quả đạt rule, synthesis và equivalence.

## Choose an installation method / Chọn cách cài đặt

### 1. Use the repository directly / Dùng trực tiếp repository

Open this repository as the workspace in Codex or Claude Code. The project skills under .agents/skills and .claude/skills are discovered in their respective tools. This is the easiest team setup.

Mở repository này làm workspace trong Codex hoặc Claude Code. Mỗi công cụ tự nhận diện skill tại thư mục tương ứng .agents/skills hoặc .claude/skills. Đây là cách đơn giản nhất khi dùng theo nhóm.

If you are setting up another machine, clone the repository first using its Git URL, then open the cloned repository in the tool.

Nếu cài trên máy khác, hãy clone repository bằng Git URL rồi mở bản clone bằng công cụ tương ứng.

### 2. Copy one skill manually into a project / Chép thủ công một skill vào project

Copy the full skill folder, keeping SKILL.md at the same relative location. In File Explorer, copy from .agents/skills/<skill-name> to the target project’s .agents/skills/<skill-name> for Codex, or from .claude/skills/<skill-name> to .claude/skills/<skill-name> for Claude Code.

Chép toàn bộ thư mục skill và giữ nguyên vị trí của SKILL.md. Trong File Explorer, chép .agents/skills/<skill-name> vào .agents/skills/<skill-name> của project đích cho Codex; với Claude Code, chép từ .claude/skills/<skill-name> vào .claude/skills/<skill-name> của project đích.

Example for Codex on Windows / Ví dụ cài cho Codex trên Windows:

    $repo = (Resolve-Path ".").Path # Run from the repository root
    $project = Read-Host "Enter the target project directory"
    $skill = "rtl-hierarchy-diagram"
    $dest = Join-Path $project ".agents\skills\$skill"
    if (Test-Path $dest) { throw "Destination exists; review it before copying." }
    New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
    Copy-Item -Recurse (Join-Path $repo ".agents\skills\$skill") $dest

Example for Claude Code on Windows / Ví dụ cài cho Claude Code trên Windows:

    $repo = (Resolve-Path ".").Path # Run from the repository root
    $project = Read-Host "Enter the target project directory"
    $skill = "rtl-hierarchy-diagram"
    $dest = Join-Path $project ".claude\skills\$skill"
    if (Test-Path $dest) { throw "Destination exists; review it before copying." }
    New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
    Copy-Item -Recurse (Join-Path $repo ".claude\skills\$skill") $dest

Replace rtl-hierarchy-diagram with any other skill name listed above to copy that skill. If the destination already exists, compare or back it up before replacing it.

Thay rtl-hierarchy-diagram bằng tên skill khác trong bảng trên để chép skill đó. Nếu thư mục đích đã tồn tại, hãy so sánh hoặc sao lưu trước khi thay thế.

### 3. Install manually for your user / Cài thủ công cho tài khoản cá nhân

For Codex, copy a skill into the user skills directory scanned by your installed Codex version. Current Codex documentation lists $HOME/.agents/skills/<skill-name>. The Codex Skill Installer may instead use $CODEX_HOME/skills; its default is commonly $HOME/.codex/skills. Check /skills after copying. For Claude Code, copy the skill folder to $HOME/.claude/skills/<skill-name>. These locations make the skill available across projects on that machine.

Với Codex, chép skill vào thư mục cá nhân mà phiên bản Codex đang cài nhận diện. Tài liệu Codex hiện tại ghi $HOME/.agents/skills/<skill-name>. Codex Skill Installer có thể dùng $CODEX_HOME/skills, mặc định thường là $HOME/.codex/skills. Kiểm tra bằng /skills sau khi chép. Với Claude Code, chép thư mục skill vào $HOME/.claude/skills/<skill-name>. Cách này giúp dùng skill qua nhiều project trên cùng máy.

Example in PowerShell / Ví dụ PowerShell:

    $repo = (Resolve-Path ".").Path # Run from the repository root
    $skill = "vlsit-rtl-spec-change-implementer"
    $dest = Join-Path $HOME ".agents\skills\$skill"
    if (Test-Path $dest) { throw "Destination exists; review it before copying." }
    New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
    Copy-Item -Recurse (Join-Path $repo ".agents\skills\$skill") $dest

For Claude Code, use .claude\skills instead of .agents\skills in both source and destination. / Với Claude Code, thay .agents\skills bằng .claude\skills ở cả thư mục nguồn và đích.

### 4. Install a GitHub-hosted skill with Codex / Cài skill từ GitHub bằng Codex

If the repository is pushed to GitHub and Codex’s skill-installer is available, invoke it and provide the repository owner/name and the exact skill directory. For example: “$skill-installer Install vlsit-rtl-spec-change-implementer from <OWNER>/<REPOSITORY>, path .agents/skills/vlsit-rtl-spec-change-implementer.” This method is for a GitHub-hosted repository; use manual copy for a local-only folder.

Nếu repository đã được đẩy lên GitHub và Codex có skill-installer, gọi skill đó rồi cung cấp owner/name của repository và đường dẫn thư mục skill chính xác. Ví dụ: “$skill-installer Install vlsit-rtl-spec-change-implementer from <OWNER>/<REPOSITORY>, path .agents/skills/vlsit-rtl-spec-change-implementer.” Cách này dành cho repository trên GitHub; nếu thư mục chỉ có trên máy, hãy chép thủ công.

### 5. Load Claude Code skills for one session / Nạp skill Claude Code trong một phiên

When working outside this repository, start Claude Code with this repository as an added directory:

    $repo = (Resolve-Path ".").Path # Run from the repository root
    claude --add-dir $repo

Claude Code loads the .claude/skills directory from the added location for that session. / Claude Code sẽ nạp thư mục .claude/skills từ vị trí được thêm trong phiên đó.

### 6. Package as a plugin for managed distribution / Đóng gói plugin để phân phối

Codex plugins and Claude Code plugins can distribute skills with a plugin manifest and, optionally, a marketplace. This repository currently contains standalone skill folders, not ready-to-install plugin packages. Packaging and publishing are separate steps. / Plugin Codex và Claude Code có thể phân phối skill qua manifest và marketplace. Repository này hiện chứa các thư mục skill độc lập, chưa phải gói plugin cài đặt sẵn. Đóng gói và phát hành là các bước riêng.

## Invoke after setup / Gọi skill sau khi cài

- Codex CLI: explicitly type $skill-name or describe the task and let Codex select a matching skill. Use /skills to view available skills; if a new skill does not appear, restart Codex. / Gọi trực tiếp bằng $skill-name hoặc mô tả yêu cầu để Codex tự chọn. Dùng /skills để xem skill; nếu skill mới chưa xuất hiện, khởi động lại Codex.
- Claude Code: type /skill-name or describe the task and let Claude choose it. Use /skills to see loaded skills. / Gõ /skill-name hoặc mô tả yêu cầu để Claude tự chọn. Dùng /skills để xem các skill đã nạp.

## Official documentation / Tài liệu chính thức

- [Codex skills, local locations, and installation](https://developers.openai.com/codex/skills)
- [Claude Code skills and loading scopes](https://code.claude.com/docs/en/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins/overview)
- [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins)
