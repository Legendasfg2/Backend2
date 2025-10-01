def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    print("Введите 'q' для выхода")

    while True:
        operation = input("\nВыберите операцию (+, -, *, /) или 'q' для выхода: ")

        if operation == 'q':
            print("Выход из калькулятора.")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Некорректная операция. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите корректное число.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2

        print(f"Результат: {num1} {operation} {num2} = {result}")

# Запуск калькулятора
calculator()
