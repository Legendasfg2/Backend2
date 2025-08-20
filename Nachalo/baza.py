# Мини-база студентов с вводом данных

students = []  # пустой список студентов

# Сколько студентов хотим ввести
n = int(input("Сколько студентов добавить? "))

for i in range(n):
    print(f"\nСтудент №{i+1}")
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    gpa = float(input("Введите средний балл: "))

    student = {"name": name, "age": age, "gpa": gpa}
    students.append(student)

# Вывод всех студентов
print("\nСписок студентов:")
for s in students:
    print(f"Имя: {s['name']}, Возраст: {s['age']}, Средний балл: {s['gpa']}")
