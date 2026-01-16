def input_matrix(name):
    """Ввод матрицы с клавиатуры"""
    rows = int(input(f"Введите количество строк для матрицы {name}: "))
    cols = int(input(f"Введите количество столбцов для матрицы {name}: "))
    print(f"Введите элементы матрицы {name} построчно (через пробел):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        while len(row) != cols:
            print(f"❌ Нужно {cols} элементов!")
            row = list(map(float, input(f"Строка {i+1}: ").split()))
        matrix.append(row)
    return matrix, rows, cols


def print_matrix(M):
    """Красивый вывод матрицы"""
    for row in M:
        print(" ".join(f"{val:7.2f}" for val in row))
    print()


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mul_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # проверка на возможность умножения
    if cols_A != rows_B:
        raise ValueError("❌ Умножение невозможно: число столбцов A != числу строк B")

    C = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def main():
    print("=== Калькулятор матриц ===")
    A, ra, ca = input_matrix("A")
    B, rb, cb = input_matrix("B")

    action = input("Выберите действие (+, -, *): ")

    try:
        if action == "+":
            if ra == rb and ca == cb:
                C = add_matrices(A, B)
            else:
                print("❌ Сложение возможно только для матриц одинакового размера")
                return
        elif action == "-":
            if ra == rb and ca == cb:
                C = sub_matrices(A, B)
            else:
                print("❌ Вычитание возможно только для матриц одинакового размера")
                return
        elif action == "*":
            C = mul_matrices(A, B)
        else:
            print("❌ Неизвестная операция")
            return

        print("\nРезультат:")
        print_matrix(C)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
