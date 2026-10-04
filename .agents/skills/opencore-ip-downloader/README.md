# OpenCores IP Downloader — Codex CLI

## Purpose / Mục đích

Find distinct, clearly licensed open-source hardware IP projects with actual RTL and collect their full project packages.

Tìm các dự án IP phần cứng mã nguồn mở khác nhau, có giấy phép rõ ràng và RTL thực, rồi thu thập đầy đủ gói dự án.

## Functions / Chức năng

- Search OpenCores and linked upstream repositories for candidates. / Tìm dự án trên OpenCores và các repository upstream được liên kết.
- Check the requested function, RTL presence, license, and whether candidates are true distinct projects. Exclude software-only projects. / Kiểm tra chức năng, RTL, giấy phép và tính độc lập của dự án; loại dự án chỉ có software.
- Download project sources and collateral; write provenance and a side-by-side README evaluation of features, functions, status, FPGA capability, and ASIC readiness. / Tải mã nguồn và tài liệu; tạo thông tin nguồn gốc cùng README so sánh features, functions, status, khả năng FPGA và mức độ sẵn sàng ASIC.

## Inputs / Đầu vào

Provide the IP type/use case, number of distinct implementations, and absolute destination folder. / Cung cấp loại IP/tình huống sử dụng, số bản triển khai khác nhau và đường dẫn tuyệt đối tới thư mục lưu.

## Use / Cách gọi

    $opencore-ip-downloader Find two distinct, clearly licensed APB UART IP cores with RTL. Save them under <ABSOLUTE_DESTINATION_DIRECTORY>.

Instructions: [SKILL.md](SKILL.md)

## Installation options / Các cách cài đặt

1. **Use this repository / Dùng repository này:** Open this repository in Codex; its .agents/skills folder is project-scoped and can be shared with the team. / Mở repository này trong Codex; skill trong .agents/skills áp dụng cho project và có thể chia sẻ với nhóm.
2. **Manual project copy / Chép thủ công vào project:** Copy this entire folder to the target project at .agents/skills/opencore-ip-downloader. / Chép toàn bộ thư mục này vào .agents/skills/opencore-ip-downloader trong project đích.
3. **Personal installation / Cài cho tài khoản cá nhân:** Copy the folder to the user skill location scanned by your Codex version. Current docs list $HOME/.agents/skills/opencore-ip-downloader; Codex Skill Installer may use $CODEX_HOME/skills. / Chép thư mục vào vị trí skill cá nhân mà phiên bản Codex nhận diện. Tài liệu hiện tại ghi $HOME/.agents/skills/opencore-ip-downloader; Codex Skill Installer có thể dùng $CODEX_HOME/skills.
4. **GitHub installer / Cài từ GitHub:** For a GitHub-hosted copy, use $skill-installer and supply the repository and .agents/skills/opencore-ip-downloader path. For local-only files, use manual copy. / Nếu skill được lưu trên GitHub, dùng $skill-installer và cung cấp repository cùng đường dẫn .agents/skills/opencore-ip-downloader. Với file chỉ có trên máy, hãy chép thủ công.

Invoke with $opencore-ip-downloader or describe a matching request. Codex may also select the skill automatically. See the repository README for Windows copy commands and plugin packaging options.

Gọi bằng $opencore-ip-downloader hoặc mô tả yêu cầu phù hợp để Codex tự chọn. Xem README repository để có lệnh chép trên Windows và lựa chọn đóng gói plugin.

## Language convention / Quy định ngôn ngữ

Skill instructions, technical references, code comments, plans, reports, diagram labels, and script outputs use precise scientific and engineering English. Only README files and explicitly designated user guidelines use bilingual English–Vietnamese content.

Nội dung skill, tài liệu tham khảo kỹ thuật, comment code, kế hoạch, báo cáo, nhãn sơ đồ và đầu ra script dùng tiếng Anh khoa học và kỹ thuật chuẩn. Chỉ README và tài liệu được xác định rõ là guideline cho người dùng sử dụng song ngữ Anh–Việt.
