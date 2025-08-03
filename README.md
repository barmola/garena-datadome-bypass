# Garena DataDome Bypass

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)]()

## 📋 Mô tả

Dự án này cung cấp một triển khai Python và JavaScript để tương tác với hệ thống DataDome của Garena. Nó bao gồm việc tạo payload được mã hóa và gửi yêu cầu đến máy chủ DataDome để nhận cookie xác thực.

## ⚠️ Tuyên bố miễn trừ trách nhiệm

**Dự án này chỉ dành cho mục đích giáo dục và nghiên cứu.** Việc sử dụng các kỹ thuật hoặc mã nguồn trong dự án này để bỏ qua các biện pháp bảo mật trên bất kỳ trang web nào mà không có sự cho phép rõ ràng là vi phạm điều khoản dịch vụ của họ và có thể là bất hợp pháp. Tác giả không chịu trách nhiệm cho bất kỳ hành vi lạm dụng nào.

## 🚀 Tính năng

- ✅ Tạo payload DataDome được mã hóa
- ✅ Mô phỏng thuật toán mã hóa từ JavaScript và Python
- ✅ Gửi yêu cầu HTTP đến máy chủ DataDome
- ✅ Xử lý phản hồi và trích xuất cookie
- ✅ Hỗ trợ fingerprint data động

## 📦 Cài đặt

### Yêu cầu hệ thống

- Python 3.7 trở lên (chỉ cần cài đặt Python)
- Node.js (chỉ cần cài đặt Node.js)

### Cài đặt dependencies

```bash
# Clone repository
git clone https://github.com/yourusername/garena-datadome-bypass.git
cd garena-datadome-bypass

# Cài đặt dependencies
pip install -r requirements.txt
```

## 🛠️ Sử dụng

### Chạy script chính

```bash
# Chạy phiên bản Python
python main.py

# Hoặc chạy phiên bản JavaScript (Node.js)
node main.js
```

### Cấu hình

Trước khi chạy, bạn có thể cần điều chỉnh các thông số sau trong file `main.py`:

```python
# Thay đổi fingerprint data theo môi trường của bạn hoặc không thay đổi cũng được :v
fingerprint_data = {
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
    "pf": "Win32",
    # ... các thông số khác
}

# Cập nhật cookie nếu cần
datadome_cookie_for_payload = ".keep"  # hoặc cookie thực tế
```

## 📁 Cấu trúc dự án

```
garena-datadome-bypass/
├── main.py              # Triển khai Python chính
├── main.js              # Triển khai JavaScript gốc
├── requirements.txt     # Dependencies Python
├── package.json         # Dependencies Node.js
├── README.md           # Tài liệu này
└── node_modules/       # Node.js modules (tự động tạo)
```

## 🔧 API Reference

### DataDomeGenerator Class

Lớp chính để tạo payload DataDome.

#### Constructor
```python
DataDomeGenerator(key: str, cookie: str)
```

#### Methods

- `generate_payload(data: Dict[str, Any]) -> str`: Tạo payload được mã hóa từ dữ liệu fingerprint

### Các hàm tiện ích

- `_hash_str_to_int(s: str) -> int`: Hash chuỗi thành số nguyên
- `_prng_h(n: int) -> int`: Thuật toán PRNG
- `_custom_b64_encode_char(n: int) -> int`: Mã hóa Base64 tùy chỉnh

## 🔍 Ví dụ sử dụng

```python
from main import DataDomeGenerator, fingerprint_data

# Khởi tạo generator
generator = DataDomeGenerator(
    key="AE3F04AD3F0D3A462481A337485081",
    cookie=".keep"
)

# Tạo payload
payload = generator.generate_payload(fingerprint_data)
print(f"Generated payload: {payload[:100]}...")
```


## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Fork dự án
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 🙏 Acknowledgments

- DataDome team cho việc tạo ra hệ thống bảo mật thú vị
- Cộng đồng Python và JavaScript
- Tất cả contributors đã đóng góp vào dự án

## 📞 Liên hệ

- **Tác giả:** Vanhxyz
- **Telegram:** [@Vanhxyz](https://t.me/Vanhxyz)
- **GitHub:** [@Vanhxyz](https://github.com/Vanhxyz2810)

---

**Lưu ý:** Dự án này được tạo ra chỉ để học tập và nghiên cứu. Hãy sử dụng có trách nhiệm và tuân thủ các điều khoản dịch vụ của các trang web bạn tương tác đi tù không chịu trách nhiệm.