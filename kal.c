#include <stdio.h>

double add(double a, double b)
{
    return a + b;
}

double subtract(double a, double b)
{
    return a - b;
}

double multiply(double a, double b)
{
    return a * b;
}

double divide(double a, double b)
{
    if (b != 0)
    {
        return a / b;
    }
    else
    {
        printf("Ошибка: деление на ноль!\n");
        return 0; // возвращаем 0 как заглушку
    }
}

int main()
{
    double a, b, result;
    char operation;

    printf("Мини-калькулятор\n");
    printf("Доступные операции: +, -, *, /\n");

    printf("Введите первое число: ");
    scanf("%lf", &a);

    printf("Введите второе число: ");
    scanf("%lf", &b);

    printf("Выберите операцию (+ - * /): ");
    scanf(" %c", &operation);

    switch (operation)
    {
    case '+':
        result = add(a, b);
        break;
    case '-':
        result = subtract(a, b);
        break;
    case '*':
        result = multiply(a, b);
        break;
    case '/':
        result = divide(a, b);
        break;
    default:
        printf("Ошибка: неизвестная операция!\n");
        return 1;
    }

    printf("Результат: %.2lf\n", result);

    return 0;
}
