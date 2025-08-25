import tkinter as tk
from tkinter import messagebox

# Игроки
PLAYER_X = "Натан (X)"
PLAYER_O = "Миракром (O)"

# Хранение игры
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
scores = {"Натан": 0, "Миракром": 0}

# Проверка победы
def check_winner():
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Ход
def make_move(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player

        winner = check_winner()
        if winner or is_draw():
            end_game(winner)
        else:
            current_player = "O" if current_player == "X" else "X"

# Конец игры
def end_game(winner):
    global scores
    if winner == "X":
        messagebox.showinfo("Результат", "Натан выиграл!, а тупой манки проиграл")
        scores["Натан"] += 1
    elif winner == "O":
        messagebox.showinfo("Результат", "Тупи манки всегда проигрывает!!!!")
        scores["Натан"] += 1
    else:
        messagebox.showinfo("Результат", "Ничья! Но очко всё равно присуждается Натану!")
        scores["Натан"] += 1

    update_scoreboard()
    reset_board()

# Очистка доски
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Обновить счёт
def update_scoreboard():
    score_label["text"] = f"Счёт: Натан {scores['Натан']} — Миракром {scores['Миракром']}"

# GUI
root = tk.Tk()
root.title("Крестики-нолики")

frame = tk.Frame(root)
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", width=10, height=4,
                        command=lambda r=i, c=j: make_move(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

score_label = tk.Label(root, text="Счёт: Натан 0 — Миракром 0", font=("Arial", 14))
score_label.pack()

root.mainloop()
