import threading
import queue
import random
import time

print(">>> Программа запущена")


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
            print(f"{self.name} задаёт {student.name} вопрос: {question}")
            time.sleep(random.uniform(1, 3))
            grade = random.randint(2, 5)
            student.grade = grade
            print(f"{self.name} поставил {student.name} оценку {grade}")
            self.students_queue.task_done()


def main():
    students = [Student(n) for n in ["Alex", "Maria", "Oleg", "Sasha"]]
    examiners = ["Ivanov", "Petrova"]
    questions = ["Что такое Python?", "Что такое ООП?", "Что такое TCP/IP?"]

    q_students = queue.Queue()
    for s in students:
        q_students.put(s)

    threads = [Examiner(e, q_students, questions) for e in examiners]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\nЭкзамен завершён!")
    for s in students:
        print(f"{s.name}: {s.grade}")


if __name__ == "__main__":
    main()
