def main():
    N, x = input().split()
    N = int(N)
    x = float(x)

    coeffs = [
        float(input()) for _ in range(N + 1)
    ]  # N+1 коэффициентов (от старшей степени до x^0)

    result = 0.0
    for i in range(N):  # от старшей до первой степени
        power = N - i
        result += coeffs[i] * power * (x ** (power - 1))

    print(f"{result:.3f}")


if __name__ == "__main__":
    main()
