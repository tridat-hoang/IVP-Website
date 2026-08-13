# 🌱 IVP Website — Trung tâm Nuôi cấy mô IVP

> Website giới thiệu **Công ty CP Giống Cây Trồng và Dược Liệu IVP** — đơn vị sản xuất giống dứa MD2 bằng công nghệ nuôi cấy mô hàng đầu Việt Nam.

Trang web tĩnh, song ngữ **Việt – Anh**, giao diện hiện đại, tối ưu cho cả máy tính và điện thoại.

---

## 📖 Giới thiệu

IVP là một trong những trung tâm nuôi cấy mô giống dứa MD2 hiện đại và quy mô nhất tại Việt Nam, với phòng LAB đạt chuẩn, vườn ươm quy mô lớn và vườn khảo nghiệm thực địa. Website này là nơi giới thiệu năng lực, sản phẩm, hoạt động thực tế và thông tin liên hệ của công ty đến khách hàng, đối tác trong và ngoài nước.

Đứng đầu phòng LAB là **Tiến sĩ Hoàng Thị Giang** — người được cấp Bằng độc quyền Giải pháp hữu ích số 4132 cho quy trình nhân giống dứa lai MD2 bằng phương pháp nuôi cấy mô.

---

## 🗂️ Các trang chính

| Trang | File | Nội dung |
|-------|------|----------|
| **Trang chủ** | `index.html` | Giới thiệu phòng LAB, bằng độc quyền, vườn ươm và vườn khảo nghiệm |
| **Sản phẩm** | `products.html` | Cây giống xuất phòng LAB, xuất vườn ươm, phôi gốc — dạng thẻ kèm pop-up xem nhanh có gallery ảnh |
| **Tin tức** | `news.html` | Tin tức & phóng sự dạng thẻ, kèm video YouTube/Facebook trong từng bài |
| **Nông trang** | `members.html` | Nhật ký thực địa: trồng dứa, tưới nhỏ giọt, lên luống, vườn ươm... |
| **Liên hệ** | `contacts.html` | Nút liên hệ nhanh, thông tin, hệ thống 3 phòng LAB, bản đồ Google Maps và form gửi yêu cầu |

---

## ✨ Tính năng nổi bật

- **Song ngữ Việt / Anh** — chuyển ngôn ngữ tức thì, ghi nhớ lựa chọn của người xem.
- **Thẻ sản phẩm hiện đại** với pop-up "Xem nhanh" có thư viện ảnh phóng to.
- **Tin tức dạng card** gọn gàng, gắn trực tiếp video YouTube/Facebook.
- **Trang Liên hệ chuyên nghiệp**: nút gọi nhanh (Gọi điện · Zalo · WhatsApp · Messenger · Email), bản đồ và form gửi tin nhắn.
- **Nút liên hệ nổi** (floating) theo suốt mọi trang.
- **Xem ảnh phóng to** (lightbox) cho toàn bộ hình ảnh.
- **Responsive** — hiển thị tốt trên máy tính, máy tính bảng và điện thoại.

---

## 🧰 Công nghệ

Trang web được xây dựng bằng **HTML, CSS và JavaScript thuần** — không cần framework, không cần bước build. Chỉ cần một trình duyệt là chạy được.

- Font: **Roboto** (Google Fonts)
- Không phụ thuộc thư viện ngoài
- Toàn bộ giao diện gói gọn trong một file `styles.css`

---

## 📁 Cấu trúc thư mục

```
IVP/
├── index.html          # Trang chủ
├── products.html       # Sản phẩm
├── news.html           # Tin tức
├── members.html        # Nông trang
├── contacts.html       # Liên hệ
├── styles.css          # Toàn bộ giao diện
├── lang.js             # Chuyển đổi ngôn ngữ Việt/Anh
├── assets/
│   ├── images/         # Hình ảnh
│   └── icons/          # Icon SVG (gọi, Zalo, WhatsApp, Messenger, email, cờ)
└── docs/               # Tài liệu nội dung gốc (.docx) — không cần khi đưa web lên mạng
```

---

## ▶️ Chạy thử & Đưa lên mạng

**Xem thử trên máy:** mở trực tiếp file `index.html` bằng trình duyệt.

**Đưa lên mạng (miễn phí, nhanh nhất):**
1. Vào [app.netlify.com/drop](https://app.netlify.com/drop)
2. Kéo-thả thư mục web (các file `.html`, `styles.css`, `lang.js` và thư mục `assets/`) vào trang.
3. Web online ngay với HTTPS — sau đó có thể gắn tên miền riêng.

> Khi đưa lên mạng **không cần** upload file `.docx` và thư mục `docs/` (tài liệu nội bộ, dung lượng lớn).
> Form liên hệ hoạt động qua **Netlify Forms** khi deploy trên Netlify.

---

## 🌍 Cơ chế song ngữ

Mỗi phần tử văn bản dùng cặp thuộc tính:

- `data-lang-vi` / `data-lang-en` — cho nội dung văn bản thuần.
- `data-lang-vi-html` / `data-lang-en-html` — cho nội dung có chứa HTML (ví dụ `<br>`).

`lang.js` tự đọc các thuộc tính này và thay nội dung khi người xem bấm nút cờ. Lựa chọn ngôn ngữ được lưu để giữ nguyên khi chuyển trang.

> **Khi chỉnh sửa nội dung:** nhớ sửa cả phần `data-lang-vi`, `data-lang-en` lẫn chữ hiển thị mặc định bên trong thẻ để hai ngôn ngữ luôn khớp nhau.

---

## 📞 Thông tin liên hệ

- **Hotline / Zalo / WhatsApp:** +84 397 600 496
- **Email:** ivpagrico@gmail.com
- **Trụ sở:** Số B01-04 Chung cư Bình Phú 2 (tầng trệt), Đường Nguyễn Chích, Phường Bắc Nha Trang, Tỉnh Khánh Hòa
- **Hệ thống phòng LAB:**
  - IVP Hà Nội — Thôn An Trung, Xã Kim Anh, TP Hà Nội
  - IVP Thanh Hóa — Xã Thọ Long, Tỉnh Thanh Hóa
  - IVP Thái Hòa — Xã Đông Hiếu, Tỉnh Nghệ An
- **Facebook:** [facebook.com/CaygiongIVP](https://www.facebook.com/CaygiongIVP/)

---

<p align="center">© 2026 Công ty CP Giống Cây Trồng và Dược Liệu IVP. Bảo lưu mọi quyền lợi.</p>
