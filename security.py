import random

def generate_word_password():
    # Список слов (можно расширить)
    words = [
        "sun", "moon", "star", "sky", "cat", "dog", "tree", "river", "pacific",
        "cloud", "stone", "fire", "wind", "wolf", "light", "dark", "heart", "ocean"
    ]

    # Выбираем 2–3 случайных слова
    num_words = random.randint(2, 3)
    chosen_words = [random.choice(words) for _ in range(num_words)]

    # Склеиваем их в строку
    password = "".join(chosen_words)

    # Добавляем случайное число и символ для надёжности
    password += str(random.randint(10, 99))
    password += random.choice("!@#$%^&*?")

    return password

# Пример использования
print("Случайный пароль:", generate_word_password())
