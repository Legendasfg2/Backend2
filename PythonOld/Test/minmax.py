numbers = input("Введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]

min_num = min(numbers)
max_num = max(numbers)

print("Минимальное число:", min_num)
print("Максимальное число:", max_num)
