# Определить, является ли целое число палиндромом.
# Отрицательные числа не считаем палиндромами.

n = int(input())

if n < 0:
    print(False)
else:
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(rev == original)
