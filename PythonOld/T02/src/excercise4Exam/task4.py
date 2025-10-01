import threading
import queue
import random
import time
import os


class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None


class Examiner(threading.Thread):
    def __init__(self, name, students_queue, questions, results):
        super().__init__()
        self.name = name
        self.students_queue = students_queue
        self.questions = questions
        self.results = results

    def run(self):
        while not self.students_queue.empty():
            try:
                student = self.students_queue.get_nowait()
            except queue.Empty:
                break
            question = random.choice(self.questions)
            time.sleep(random.uniform(1, 3))
            grade = random.randint(2, 5)
            student.grade = grade
            self.results.append((student.name, self.name, grade))
            self.students_queue.task_done()


def live_display(results, students, stop_event):
    while not stop_event.is_set():
        os.system("cls" if os.name == "nt" else "clear")
        print("Текущие результаты экзамена:\n")
        for s in students:
            grade = s.grade if s.grade is not None else "-"
            print(f"{s.name:<10} | {grade}")
        time.sleep(1)


def main():
    students = [Student(n) for n in ["Alex", "Maria", "Oleg", "Sasha", "Olga"]]
    examiners = ["Ivanov", "Petrova"]
    questions = ["Что такое Python?", "Что такое ООП?", "Что такое TCP/IP?"]

    q_students = queue.Queue()
    for s in students:
        q_students.put(s)

    results = []
    stop_event = threading.Event()
    threads = [Examiner(e, q_students, questions, results) for e in examiners]

    for t in threads:
        t.start()

    display_thread = threading.Thread(
        target=live_display, args=(results, students, stop_event)
    )
    display_thread.start()

    for t in threads:
        t.join()
    stop_event.set()
    display_thread.join()

    print("\nЭкзамен завершён! Итоговые оценки:")
    for s in students:
        print(f"{s.name}: {s.grade}")


if __name__ == "__main__":
    main()
