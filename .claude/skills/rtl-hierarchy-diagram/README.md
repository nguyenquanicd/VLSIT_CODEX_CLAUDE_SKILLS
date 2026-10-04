# RTL Hierarchy Diagram — Claude Code

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

    /rtl-hierarchy-diagram Analyze the RTL in C:\work\rtl\src and create the hierarchy diagram.

Instructions: [SKILL.md](SKILL.md)

## Installation options / Các cách cài đặt

1. **Use this repository / Dùng repository này:** Open this repository in Claude Code; its .claude/skills folder is project-scoped and can be shared with the team. / Mở repository này trong Claude Code; skill trong .claude/skills áp dụng cho project và có thể chia sẻ với nhóm.
2. **Manual project copy / Chép thủ công vào project:** Copy this entire folder to the target project at .claude/skills/rtl-hierarchy-diagram. / Chép toàn bộ thư mục này vào .claude/skills/rtl-hierarchy-diagram trong project đích.
3. **Personal installation / Cài cho tài khoản cá nhân:** Copy the folder to $HOME/.claude/skills/rtl-hierarchy-diagram to make it available across local projects. / Chép thư mục vào $HOME/.claude/skills/rtl-hierarchy-diagram để dùng trong các project cục bộ.
4. **One-session loading / Nạp cho một phiên:** Start Claude Code with claude --add-dir "<path to this repository>" when working outside this repository. / Khi làm việc ngoài repository này, khởi chạy Claude Code với claude --add-dir "<đường dẫn tới repository>".
5. **Plugin installation / Cài plugin:** This skill can be installed as a plugin only after it is packaged with a Claude Code plugin manifest and marketplace or loaded plugin directory. This repository is not packaged as a plugin yet. / Chỉ có thể cài skill dạng plugin sau khi đóng gói kèm manifest Claude Code và marketplace hoặc thư mục plugin. Repository này chưa được đóng gói thành plugin.

Invoke with /rtl-hierarchy-diagram or describe a matching request. Claude Code may also select the skill automatically. Use /skills to confirm it loaded. See the repository README for Windows examples and plugin details.

Gọi bằng /rtl-hierarchy-diagram hoặc mô tả yêu cầu phù hợp để Claude Code tự chọn. Dùng /skills để xác nhận skill đã được nạp. Xem README repository để biết ví dụ Windows và thông tin plugin.
