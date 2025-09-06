import time
import sys
import msvcrt  # для работы с клавишами на Windows


def runner_game():
    print("🏃 Мини-игра 'Бегун'")
    print("Нажимай Enter, чтобы бежать к стене!")
    print("Если замешкаешься больше чем на 2 секунды → проиграл.\n")

    track_length = 30
    position = 0
    time_limit = 2  # секунды на реакцию

    while position < track_length:
        print(" " * position + "🏃" + " " * (track_length - position) + "|")

        start = time.time()
        pressed = False

        # ждём нажатия клавиши с ограничением по времени
        while time.time() - start < time_limit:
            if msvcrt.kbhit():  # если клавиша нажата
                key = msvcrt.getch()
                if key == b"\r":  # Enter
                    pressed = True
                    break
        if not pressed:
            print("⏰ Время вышло! Ты проиграл!")
            sys.exit()

        position += 1

    print("🏆 Ура! Ты добежал до стены и победил!")


if __name__ == "__main__":
    runner_game()
