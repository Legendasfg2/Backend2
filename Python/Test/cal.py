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
        # Запрашиваем операцию
        operation = input("Выберите операцию (+, -, *, /, **) или 'выход' для выхода: ").strip()

        # Проверяем выход
        if operation == 'выход':
            print("Работа калькулятора завершена.")
            break

        # Проверяем, поддерживается ли операция
        if operation not in ['+', '-', '*', '/', '**']:
            print("Ошибка: Неверная операция. Попробуйте снова.\n")
            continue

        # Обрабатываем операцию возведения в квадрат
        if operation == '**':
            try:
                num = float(input("Введите число, которое хотите возвести в квадрат: "))
                result = num ** 2
                print(f"Результат: {num}² = {result}")
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректное число.\n")
            print()  # Пустая строка для разделения
            continue  # Возвращаемся к началу цикла (новый выбор операции)

        # Для всех остальных операций (+, -, *, /) — запрашиваем два числа
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные числа.\n")
            print()
            continue

        # Выполняем операцию
        if operation == '+':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно.")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")

        print()  # Пустая строка между операциями

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
