# Skill sets for Codex and Claude Code / Bộ skill cho Codex và Claude Code

## Structure / Cấu trúc

**VI:** Bộ Codex nằm tại .agents/skills/{skill-name}/SKILL.md. Bộ Claude Code tương ứng nằm tại .claude/skills/{skill-name}/SKILL.md. Mỗi thư mục skill có file SKILL.md với metadata name và description cùng hướng dẫn thực hiện.

**EN:** The Codex set is under .agents/skills/{skill-name}/SKILL.md. The corresponding Claude Code set is under .claude/skills/{skill-name}/SKILL.md. Each skill directory contains a SKILL.md with name and description metadata followed by its instructions.

## Included skills / Skill hiện có

| Skill | Purpose / Mục đích |
|---|---|
| opencore-ip-downloader | Find and collect licensed open-source hardware IP projects. / Tìm và thu thập các dự án IP phần cứng mã nguồn mở có giấy phép rõ ràng. |
| rtl-hierarchy-diagram | Analyze RTL hierarchy and create a multi-page draw.io block diagram. / Phân tích hierarchy RTL và tạo sơ đồ khối draw.io nhiều trang. |

## Use / Cách dùng

- **Codex CLI:** invoke a skill with $opencore-ip-downloader or $rtl-hierarchy-diagram, or describe the task and let Codex select it. / Gọi skill trực tiếp bằng tên skill có tiền tố $ hoặc mô tả yêu cầu để Codex tự chọn.
- **Claude Code:** invoke the matching skill with /opencore-ip-downloader or /rtl-hierarchy-diagram, or let Claude load it when relevant. / Gọi skill bằng slash command tương ứng hoặc để Claude tự nạp khi phù hợp.
- **RTL input:** rtl-hierarchy-diagram requires the explicit path to the RTL source directory. It asks for the path if the request omits it. / Skill rtl-hierarchy-diagram yêu cầu đường dẫn rõ ràng tới thư mục RTL và sẽ hỏi nếu yêu cầu chưa cung cấp.
