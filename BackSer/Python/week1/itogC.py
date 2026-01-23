while True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /) или 'выход' для завершения: ")
    if operation == "+":
        res = num1 + num2
        print("Результат: ", res)
    elif operation == "-":
        res = num1 - num2
        print("Результат: ", res)
    elif operation == "*":
        res = num1 * num2
        print("Результат: ", res)
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно.")
        else:
            res = num1 / num2
            print("Результат: ", res)
    elif operation == "выход":
        print("Завершение программы.")
        break
