users = {}

def register():
    login = input("Введите логин: ")
    if login in users:
        print("Ошибка: логин уже существует.")
        return
    password = input("Введите пароль: ")
    users[login] = password
    print("Регистрация успешна.")

def login():
    login = input("Введите логин: ")
    if login not in users:
        print("Ошибка: логин не найден.")
        return
    password = input("Введите пароль: ")
    if users[login] == password:
        print("Вход выполнен успешно.")
    else:
        print("Ошибка: неверный пароль.")

def main():
    while True:
        choice = input("Выберите действие (register/login/exit): ").strip().lower()
        if choice == "register":
            register()
        elif choice == "login":
            login()
        elif choice == "exit":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()
