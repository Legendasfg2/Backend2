num = int(input("Введите число: "))
print(f"Нечетные числа от 1 до {num}:")
for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)
