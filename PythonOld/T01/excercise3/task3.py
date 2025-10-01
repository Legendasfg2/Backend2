# Определение количества квадратов и кругов в бинарной матрице
# Ввод: строки матрицы 0/1 через пробел
# Вывод: два числа через пробел (кол-во квадратов и кругов)

import sys
from collections import deque

lines = sys.stdin.read().strip().splitlines()
matrix = [list(map(int, line.split())) for line in lines]
n = len(matrix)

visited = [[False] * n for _ in range(n)]


def bfs(start_i, start_j):
    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = True
    cells = []

    while q:
        i, j = q.popleft()
        cells.append((i, j))

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and matrix[ni][nj] == 1:
                    visited[ni][nj] = True
                    q.append((ni, nj))
    return cells


def classify(cells):
    rows = [i for i, _ in cells]
    cols = [j for _, j in cells]
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)

    height = max_r - min_r + 1
    width = max_c - min_c + 1

    full = True
    for i in range(min_r, max_r + 1):
        for j in range(min_c, max_c + 1):
            if matrix[i][j] != 1:
                full = False
                break
        if not full:
            break

    if full and height == width:
        return "square"
    else:
        return "circle"


squares, circles = 0, 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            cells = bfs(i, j)
            if len(cells) > 1:
                if classify(cells) == "square":
                    squares += 1
                else:
                    circles += 1

print(squares, circles)
