import time

text = input("Введите предложение: ")

# Постепенное нарастание
current = ""
for char in text:
    current += char
    print(current)
    time.sleep(0.3)

# Постепенное уменьшение
for i in range(len(text) - 1, 0, -1):
    print(text[:i])
    time.sleep(0.3)
