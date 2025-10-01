import sys


def main():
    line = sys.stdin.readline().strip()

    # проверка, что строка состоит только из цифр
    if not line.isdigit():
        print("Natural number was expected")
        return

    n = int(line)
    if n <= 0:
        print("Natural number was expected")
        return

    # печатаем треугольник Паскаля
    for row in range(n):
        val = 1
        line_vals = []
        for col in range(row + 1):
            line_vals.append(str(val))
            val = val * (row - col) // (col + 1)
        print(" ".join(line_vals))


if __name__ == "__main__":
    main()
