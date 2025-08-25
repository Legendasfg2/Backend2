def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # переводим см в метры
    if height_m <= 0:
        raise ValueError("Рост должен быть больше нуля.")
    return weight_kg / (height_m ** 2)

try:
    weight = float(input("Введите ваш вес (кг): "))
    height_cm = float(input("Введите ваш рост (см): "))
    bmi = calculate_bmi(weight, height_cm)
    print(f"Ваш индекс массы тела (BMI): {bmi:.2f}")
    if bmi < 18.5:
        print("Недостаточная масса тела.")
    elif 18.5 <= bmi <= 24.99:
        print("Норма.")
    else:
        print("Избыточная масса тела или ожирение.")
except ValueError as e:
    print(f"Ошибка: {e}")
