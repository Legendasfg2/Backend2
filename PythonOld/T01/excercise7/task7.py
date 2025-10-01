def main():
    # читаем размеры поля
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    # создаем dp-таблицу
    dp = [[0] * M for _ in range(N)]

    dp[0][0] = field[0][0]

    # первая строка
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + field[0][j]

    # первый столбец
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + field[i][0]

    # остальные клетки
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = field[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    # выводим результат
    print(dp[N - 1][M - 1])


if __name__ == "__main__":
    main()
