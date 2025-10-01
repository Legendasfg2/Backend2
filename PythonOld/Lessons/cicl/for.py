text = input("Введите текст: ")
count = 0
for letter in text:
    if letter in "уеаоэяиюУЕЫАОЭЯИЮeyuioaEYUIOA":
        count += 1
print("Количество гласных в тексте: ", count)
