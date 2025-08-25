def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Проверка на палиндром
    # Сравниваем очищенную строку с её обратной версией
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]
input_str = input("Введите строку: ")
if is_palindrome(input_str):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
