import random

secret_number = random.randint(1, 10)
attempts = 0

print("Я загадал число от 1 до 10!")
print("Попробуй угадать")

while True:
    guess = input("Введи число: ")

    if not guess.isdigit():
        print("Нужно ввести число, а не буквы.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Моё число больше.")
    elif guess > secret_number:
        print("Моё число меньше.")
    else:
        print("Ты угадал!")
        print("Попыток:", attempts)
        break
