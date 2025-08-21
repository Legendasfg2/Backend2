import sys

s = sys.stdin.readline().strip()

# проверяем формат
if not s:
    print("Incorrect input")
    sys.exit()

sign = 1
if s[0] in "+-":
    if s[0] == "-":
        sign = -1
    s = s[1:]

if not s or s == ".":
    print("Incorrect input")
    sys.exit()

if s.count(".") > 1:
    print("Incorrect input")
    sys.exit()

# разделяем целую и дробную части
if "." in s:
    int_part, frac_part = s.split(".")
else:
    int_part, frac_part = s, ""

if not (int_part.isdigit() or (int_part == "" and frac_part)):
    print("Incorrect input")
    sys.exit()

if frac_part and not frac_part.isdigit():
    print("Incorrect input")
    sys.exit()

# переводим строку в число вручную
value = 0

# целая часть
for ch in int_part:
    if ch:
        value = value * 10 + (ord(ch) - ord("0"))

# дробная часть
frac_value = 0
power = 1
for ch in frac_part:
    power *= 10
    frac_value += (ord(ch) - ord("0")) / power

result = sign * (value + frac_value)

# умножаем на 2
result *= 2

# выводим с 3 знаками
print(f"{result:.3f}")
