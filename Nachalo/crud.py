tasks = []

def add_task(task):
    tasks.append(task)
    print("Задача добавлена.")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Задача '{removed}' удалена.")
    else:
        print("Некорректный номер задачи.")

def main():
    while True:
        print("\n1. Добавить задачу")
        print("2. Посмотреть все задачи")
        print("3. Удалить задачу по номеру")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            try:
                number = int(input("Введите номер задачи для удаления: "))
                delete_task(number)
            except ValueError:
                print("Введите корректный номер.")
        elif choice == '4':
            print("Выход.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
