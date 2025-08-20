def main():
    N = int(input())  # читаем количество чисел
    numbers = set()  # создаём пустое множество для уникальных чисел

    for _ in range(N):
        num = int(input())
        numbers.add(
            num
        )  # добавляем число во множество (дубликаты автоматически игнорируются)

    print(len(numbers))  # количество различных чисел


if __name__ == "__main__":
    main()
