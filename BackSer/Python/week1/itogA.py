name = input("Твоё имя: ")
age = int(input("Твой возраст: "))
height = float(input("Рост в см: "))
city = input("Город проживания: ")
print("\n--------Твоя Анкета--------")
print("Имя: ", name)
print("Возраст: ", age)
print("Рост: ", height)
print("Город: ", city)
if age < 18:
    print("Молодой")
elif age >= 18 and age <= 25:
    print("Студент")
else:
    print("Взрослый")
