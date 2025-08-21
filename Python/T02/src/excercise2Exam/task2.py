from collections import deque


class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None


class Examiner:
    def __init__(self, name):
        self.name = name


class Question:
    def __init__(self, text):
        self.text = text


def main():
    students = deque([Student(n) for n in ["Alex", "Maria", "Oleg"]])
    examiners = [Examiner(n) for n in ["Ivanov", "Petrova"]]
    questions = [Question(q) for q in ["Что такое Python?", "Объясните принцип ООП"]]

    print("Студенты в очереди:", [s.name for s in students])
    print("Экзаменаторы:", [e.name for e in examiners])
    print("Вопросы:", [q.text for q in questions])


if __name__ == "__main__":
    main()
