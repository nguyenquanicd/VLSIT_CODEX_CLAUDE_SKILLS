# VLSIT RTL Hierarchy Diagram — Codex CLI

## Purpose / Mục đích

Trace an existing RTL design from its top module through submodules and show hierarchy and important functional connections in an editable Draw.io diagram.

Lần theo thiết kế RTL hiện có từ module top tới các module con, thể hiện hierarchy và kết nối chức năng quan trọng trong sơ đồ Draw.io có thể chỉnh sửa.

## Functions / Chức năng

- Map module instances and parent-child relationships by hierarchy depth. / Liệt kê instance và quan hệ cha-con theo từng cấp hierarchy.
- Trace important interfaces and functional paths such as AXI/APB, handshakes, interrupts, and data/control links. / Lần theo interface và đường chức năng như AXI/APB, handshake, interrupt, data/control.
- Add a concise module-function/interface panel to each page; use black-and-white styling and 18 pt text. / Thêm khung ngắn mô tả chức năng/interface của module trên mỗi trang; dùng hai màu đen trắng và chữ 18 pt.

## Input and output / Đầu vào và đầu ra

An explicit RTL source-directory path is required. The default deliverable is a multi-page rtl_hierarchy.drawio file. The skill analyzes RTL but does not modify it.

Bắt buộc cung cấp đường dẫn thư mục RTL cụ thể. Kết quả mặc định là file rtl_hierarchy.drawio nhiều trang. Skill phân tích RTL nhưng không sửa mã nguồn.

## Use / Cách gọi

    $vlsit-rtl-hierarchy-diagram Analyze the RTL in <RTL_SOURCE_DIRECTORY> and create the hierarchy diagram.

Instructions: [SKILL.md](SKILL.md)

## Installation options / Các cách cài đặt

1. **Use this repository / Dùng repository này:** Open this repository in Codex; its .agents/skills folder is project-scoped and can be shared with the team. / Mở repository này trong Codex; skill trong .agents/skills áp dụng cho project và có thể chia sẻ với nhóm.
2. **Manual project copy / Chép thủ công vào project:** Copy this entire folder to the target project at .agents/skills/vlsit-rtl-hierarchy-diagram. / Chép toàn bộ thư mục này vào .agents/skills/vlsit-rtl-hierarchy-diagram trong project đích.
3. **Personal installation / Cài cho tài khoản cá nhân:** Copy the folder to the user skill location scanned by your Codex version. Current docs list $HOME/.agents/skills/vlsit-rtl-hierarchy-diagram; Codex Skill Installer may use $CODEX_HOME/skills. / Chép thư mục vào vị trí skill cá nhân mà phiên bản Codex nhận diện. Tài liệu hiện tại ghi $HOME/.agents/skills/vlsit-rtl-hierarchy-diagram; Codex Skill Installer có thể dùng $CODEX_HOME/skills.
4. **GitHub installer / Cài từ GitHub:** For a GitHub-hosted copy, use $skill-installer and supply the repository and .agents/skills/vlsit-rtl-hierarchy-diagram path. For local-only files, use manual copy. / Nếu skill được lưu trên GitHub, dùng $skill-installer và cung cấp repository cùng đường dẫn .agents/skills/vlsit-rtl-hierarchy-diagram. Với file chỉ có trên máy, hãy chép thủ công.

Invoke with $vlsit-rtl-hierarchy-diagram or describe a matching request. Codex may also select the skill automatically. See the repository README for Windows copy commands and plugin packaging options.

Gọi bằng $vlsit-rtl-hierarchy-diagram hoặc mô tả yêu cầu phù hợp để Codex tự chọn. Xem README repository để có lệnh chép trên Windows và lựa chọn đóng gói plugin.

## Language convention / Quy định ngôn ngữ

Skill instructions, technical references, code comments, plans, reports, diagram labels, and script outputs use precise scientific and engineering English. Only README files and explicitly designated user guidelines use bilingual English–Vietnamese content.

Nội dung skill, tài liệu tham khảo kỹ thuật, comment code, kế hoạch, báo cáo, nhãn sơ đồ và đầu ra script dùng tiếng Anh khoa học và kỹ thuật chuẩn. Chỉ README và tài liệu được xác định rõ là guideline cho người dùng sử dụng song ngữ Anh–Việt.
