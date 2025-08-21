def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def main():
    examiners = read_file("examiners.txt")
    students = read_file("students.txt")
    questions = read_file("questions.txt")

    print("Экзаменаторы:", examiners)
    print("Студенты:", students)
    print("Вопросы:", questions)


if __name__ == "__main__":
    main()
