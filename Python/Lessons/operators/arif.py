num1 = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неизвестная операция"

print("Результат:", result)
