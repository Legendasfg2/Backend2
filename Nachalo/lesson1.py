numbers = input("Введите числа через пробел: ")
numbers = list(map(int, numbers.split()))  # преобразуем ввод в список чисел
total = sum(numbers)

print("Сумма чисел =", total)
