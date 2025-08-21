import threading
import queue
import random
import time
import statistics


class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None


class Examiner(threading.Thread):
    def __init__(self, name, students_queue, questions):
        super().__init__()
        self.name = name
        self.students_queue = students_queue
        self.questions = questions

    def run(self):
        while not self.students_queue.empty():
            try:
                student = self.students_queue.get_nowait()
            except queue.Empty:
                break
            question = random.choice(self.questions)
            time.sleep(random.uniform(1, 2))
            grade = random.randint(2, 5)
            student.grade = grade
            print(f"{self.name} проверил {student.name}, оценка: {grade}")
            self.students_queue.task_done()


def main():
    students = [
        Student(n) for n in ["Alex", "Maria", "Oleg", "Sasha", "Olga", "Dmitry"]
    ]
    examiners = ["Ivanov", "Petrova", "Sidorov"]
    questions = [
        "Что такое Python?",
        "Что такое ООП?",
        "Что такое TCP/IP?",
        "Что такое база данных?",
    ]

    q_students = queue.Queue()
    for s in students:
        q_students.put(s)

    threads = [Examiner(e, q_students, questions) for e in examiners]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\nЭкзамен завершён! Итоговые оценки:")
    grades = []
    for s in students:
        print(f"{s.name}: {s.grade}")
        grades.append(s.grade)

    print("\nСтатистика:")
    print("Средний балл:", statistics.mean(grades))
    print("Максимальный балл:", max(grades))
    print("Минимальный балл:", min(grades))


if __name__ == "__main__":
    main()
