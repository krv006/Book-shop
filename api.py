import requests

# Sahifani olish
a = requests.get('https://bank.uz/uz/currency')

# Agar muvaffaqiyatli bo'lsa (status code 200)
if a.status_code == 200:
    print(a.text)  # Sahifaning HTML kodi
else:
    print(f"Xato: {a.status_code}")

# requests.get('https://bank.uz/uz/currency')
