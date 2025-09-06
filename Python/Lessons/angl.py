import json
import random
import os

FILENAME = "dictionary.json"


def load_dictionary():
    """Загружает словарь из JSON-файла. Если файла нет — возвращает пустой словарь."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Ошибка чтения файла. Создаём новый словарь.")
                return {}
    return {}


def save_dictionary(dictionary):
    """Сохраняет словарь в JSON-файл."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)


def add_word(dictionary):
    """Добавляет новое слово и его перевод в словарь."""
    english = input("Введите английское слово: ").strip()
    if not english:
        print("Слово не может быть пустым.")
        return
    russian = input("Введите перевод на русский: ").strip()
    if not russian:
        print("Перевод не может быть пустым.")
        return

    dictionary[english] = russian
    print(f"Добавлено: {english} — {russian}")


def test_words(dictionary):
    """Проводит тест: показывает английское слово, пользователь вводит перевод."""
    if not dictionary:
        print("Словарь пуст. Сначала добавьте слова.")
        return

    words = list(dictionary.items())
    random.shuffle(words)  # Перемешиваем слова

    correct = 0
    total = len(words)

    print("\n--- Начинаем тест! Введите 'стоп', чтобы закончить ---\n")

    for i, (eng, rus) in enumerate(words, 1):
        print(f"Вопрос {i}: {eng}")
        answer = input("Ваш перевод: ").strip()

        if answer.lower() == "стоп":
            print("Тест прерван.")
            break

        if answer == rus:
            print("✅ Правильно!")
            correct += 1
        else:
            print(f"❌ Неправильно. Правильный ответ: {rus}")

        print("-" * 40)

    if i > 0:  # Если были вопросы
        print(f"\nРезультат: {correct}/{total} правильных ответов.")


def main():
    dictionary = load_dictionary()

    while True:
        print("\n--- Меню ---")
        print("1. Добавить слово")
        print("2. Пройти тест")
        print("3. Показать весь словарь")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            add_word(dictionary)
            save_dictionary(dictionary)
        elif choice == "2":
            test_words(dictionary)
        elif choice == "3":
            if dictionary:
                print("\n--- Ваш словарь ---")
                for eng, rus in dictionary.items():
                    print(f"{eng} — {rus}")
            else:
                print("Словарь пуст.")
        elif choice == "4":
            print("Сохраняем и выходим...")
            save_dictionary(dictionary)
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
