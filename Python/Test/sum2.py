number = input("Введите число: ")
digit_sum = sum(int(digit) for digit in number if digit.isdigit())
print("Сумма цифр:", digit_sum)
