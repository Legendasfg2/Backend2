def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("+ — сложение")
    print("- — вычитание")
    print("* — умножение")
    print("/ — деление")
    print("** — возведение в квадрат (число²)")
    print("Введите 'выход', чтобы завершить программу.\n")

    while True:
        operation = input(
            "Выберите операцию (+, -, *, /, **) или 'выход' для выхода: "
        ).strip()
        if operation == "выход":
            print("Работа калькулятора завершена.")
            break
        if operation not in ["+", "-", "*", "/", "**"]:
            print("Ошибка: Неверная операция. Попробуйте снова.\n")
            continue
        if operation == "**":
            try:
                num = float(input("Введите число, которое хотите возвести в квадрат: "))
                result = num**2
                print(f"Результат: {num}² = {result}")
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректное число.\n")
            print()
            continue
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные числа.\n")
            print()
            continue
        if operation == "+":
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно.")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")

        print()
if __name__ == "__main__":
    calculator()
