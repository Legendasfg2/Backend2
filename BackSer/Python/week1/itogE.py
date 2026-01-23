num = int(input("Введите целое число: "))
count = 0
total = 0
while True:
    if num == 0:
        print("Вы ввели ноль, программа завершена.")
        break
    total += num
    count += 1

    if num % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")
    if num > 0:
        print("Положительное")
    else:
        print("Отрицательное")
    print(f"Количество введенных чисел: {count}")
    print(f"Сумма введенных чисел: {total}")
    avg = total / count
    print(f"Среднее арифметическое введенных чисел: {avg}")
    num = int(input("Введите целое число: "))
    count += 1

