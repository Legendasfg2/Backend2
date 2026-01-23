def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "На 0 делить нельзя."
    return x / y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Числа а не буквы.")

def display_menu():
    print("\nВыберите действия:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. Выход")

def main():
    while True:
        display_menu()
        choice = input("Выберите операцию (1/2/3/4/5): ")

        if choice == '5':
            print("ББ")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = get_number_input("Введите первое число: ")
            num2 = get_number_input("Введите второе число: ")

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Введите число между 1 и 5, пожалуйста.")

if __name__ == "__main__":
    main()
