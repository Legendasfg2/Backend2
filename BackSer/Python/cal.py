ch = float(input("Введите ваше чиссло: "))
ch2 = float(input("Введите второе чиссло: "))
op = input("введите вашу операцию: + - * / \n")
if op == "-":
    result = ch - ch2
elif op == "+":
    result = ch + ch2
elif op == "*":
    result = ch * ch2
elif op == "/":
    if ch2 == 0:
        result = "Делить на 0 нельзя"
    else:
        result = ch / ch2
else:
    result = "Неверная операция"
print("Результат: ", result)
