accounts = {"Натан": 1000}


def parse_amount(text):
    """Преобразует строку с суммой в число (удаляет пробелы и запятые)."""
    return int(text.replace(" ", "").replace(",", ""))


def show_menu():
    print("\n--- Мини-банк ---")
    print("1. Проверить баланс")
    print("2. Пополнить счёт")
    print("3. Снять деньги")
    print("4. Выйти")


print("Добро пожаловать в мини-банк!")

# Вход или регистрация
name = input("Введите своё имя: ")

if name not in accounts:
    print("Такого пользователя нет.")
    register = input("Хотите зарегистрироваться? (да/нет): ").lower()
    if register == "да":
        accounts[name] = 0
        print(f"Пользователь {name} зарегистрирован! Баланс: 0")
    else:
        print("Без регистрации вход невозможен. Выход...")
        exit()

# Главное меню
while True:
    show_menu()
    choice = input("Выберите пункт меню (1-4): ")

    if choice == "1":
        print(f"Ваш баланс: {accounts[name]:,}".replace(",", " "))

    elif choice == "2":
        raw = input("Введите сумму для пополнения: ")
        amount = parse_amount(raw)
        if amount > 0:
            accounts[name] += amount
            print(f"Счёт пополнен на {amount:,}".replace(",", " "))
            print(f"Баланс: {accounts[name]:,}".replace(",", " "))
        else:
            print("Сумма должна быть положительной!")

    elif choice == "3":
        raw = input("Введите сумму для снятия: ")
        amount = parse_amount(raw)
        if amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Вы сняли {amount:,}".replace(",", " "))
            print(f"Баланс: {accounts[name]:,}".replace(",", " "))
        else:
            print("Недостаточно средств!")

    elif choice == "4":
        print("Выход из программы. До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
