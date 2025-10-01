import random


def guess_number():
    print("Добро пожаловать в игру 'Угадай число' 🎲")

    while True:
        print("\nВыбери уровень сложности:")
        print("1. Лёгкий (1-10)")
        print("2. Средний (1-50)")
        print("3. Сложный (1-100)")

        choice = input("Введите 1, 2 или 3: ")

        if choice == "1":
            number = random.randint(1, 10)
            max_num = 10
        elif choice == "2":
            number = random.randint(1, 50)
            max_num = 50
        elif choice == "3":
            number = random.randint(1, 100)
            max_num = 100
        else:
            print("❌ Ошибка: введите 1, 2 или 3")
            continue

        print(f"\nЯ загадал число от 1 до {max_num}. Попробуй угадать!")

        attempts = 0
        while True:
            try:
                guess = int(input("Введите число: "))
                attempts += 1

                if guess < number:
                    print("Больше!")
                elif guess > number:
                    print("Меньше!")
                else:
                    print(f"🎉 Поздравляю! Ты угадал число за {attempts} попыток!")
                    break
            except ValueError:
                print("Введите число цифрами!")

        again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за игру! 👋")
            break


# запуск
if __name__ == "__main__":
    guess_number()
