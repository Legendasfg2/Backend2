import sys


def read_vector():
    parts = sys.stdin.readline().strip().split()
    return [float(parts[0]), float(parts[1]), float(parts[2])]


v1 = read_vector()
v2 = read_vector()

result = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
print(result)
