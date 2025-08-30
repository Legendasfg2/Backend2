secure = input("Введите пароль: ")
if secure == "admin" or secure == "root":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
