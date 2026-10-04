# VLSIT RTL Specification Change Implementer — Codex CLI

## Purpose / Mục đích

Analyze existing RTL against a new feature request and optional old specification; propose minimal changes, wait for sign-off, then implement the approved plan.

Phân tích RTL hiện có theo yêu cầu tính năng mới và specification cũ nếu có; đề xuất thay đổi tối thiểu, chờ ký duyệt, rồi triển khai kế hoạch đã được chấp thuận.

## Functions / Chức năng

- Map requirements to current RTL behavior and affected modules/files. / Đối chiếu yêu cầu với hành vi RTL hiện tại và xác định module/file bị ảnh hưởng.
- Document why each edit is needed, unresolved questions, and up to three viable approaches when there are meaningful alternatives. / Ghi rõ lý do từng thay đổi, câu hỏi còn mở và tối đa ba phương án nếu có lựa chọn đáng kể.
- Stop at a bilingual review gate before editing RTL. After approval, make only approved changes and report the diff-based RTL code-change percentage. / Dừng tại cổng duyệt song ngữ trước khi sửa RTL. Sau khi duyệt, chỉ sửa phần đã chấp thuận và báo cáo tỷ lệ code RTL thay đổi dựa trên diff.

## Inputs and output / Đầu vào và đầu ra

The RTL directory is required. The old specification is optional. Provide a new specification file or describe the requested feature in the prompt. The skill creates rtl_change_review.md and updates it with implementation results.

Bắt buộc có thư mục RTL. Specification cũ là tùy chọn. Cung cấp file specification mới hoặc mô tả tính năng trong prompt. Skill tạo rtl_change_review.md và cập nhật file này với kết quả triển khai.

## Use / Cách gọi

    $vlsit-rtl-spec-change-implementer Analyze C:\work\rtl\src for the described feature. Old spec: none. Prepare a bilingual plan and wait for sign-off.

Instructions: [SKILL.md](SKILL.md)

## Installation options / Các cách cài đặt

1. **Use this repository / Dùng repository này:** Open this repository in Codex; its .agents/skills folder is project-scoped and can be shared with the team. / Mở repository này trong Codex; skill trong .agents/skills áp dụng cho project và có thể chia sẻ với nhóm.
2. **Manual project copy / Chép thủ công vào project:** Copy this entire folder to the target project at .agents/skills/vlsit-rtl-spec-change-implementer. / Chép toàn bộ thư mục này vào .agents/skills/vlsit-rtl-spec-change-implementer trong project đích.
3. **Personal installation / Cài cho tài khoản cá nhân:** Copy the folder to the user skill location scanned by your Codex version. Current docs list $HOME/.agents/skills/vlsit-rtl-spec-change-implementer; Codex Skill Installer may use $CODEX_HOME/skills. / Chép thư mục vào vị trí skill cá nhân mà phiên bản Codex nhận diện. Tài liệu hiện tại ghi $HOME/.agents/skills/vlsit-rtl-spec-change-implementer; Codex Skill Installer có thể dùng $CODEX_HOME/skills.
4. **GitHub installer / Cài từ GitHub:** For a GitHub-hosted copy, use $skill-installer and supply the repository and .agents/skills/vlsit-rtl-spec-change-implementer path. For local-only files, use manual copy. / Nếu skill được lưu trên GitHub, dùng $skill-installer và cung cấp repository cùng đường dẫn .agents/skills/vlsit-rtl-spec-change-implementer. Với file chỉ có trên máy, hãy chép thủ công.

Invoke with $vlsit-rtl-spec-change-implementer or describe a matching request. Codex may also select the skill automatically. See the repository README for Windows copy commands and plugin packaging options.

Gọi bằng $vlsit-rtl-spec-change-implementer hoặc mô tả yêu cầu phù hợp để Codex tự chọn. Xem README repository để có lệnh chép trên Windows và lựa chọn đóng gói plugin.
