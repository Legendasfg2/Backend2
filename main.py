import re

def parse_numbers(s: str):
    # Разрешаем разделители: пробелы, запятые, точки с запятой
    tokens = re.split(r'[,\s;]+', s.strip())
    nums = []
    for t in tokens:
        if not t:
            continue
        try:
            # Если целое — парсим как int, иначе как float
            if re.fullmatch(r'[+-]?\d+', t):
                nums.append(int(t))
            else:
                nums.append(float(t))
        except ValueError:
            # Игнорируем мусорные токены
            pass
    return nums

def unique_preserve_order(values):
    seen = set()
    out = []
    for v in values:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out

def fmt(n):
    # Красиво печатаем: 2.0 -> 2
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

if __name__ == "__main__":
    print("Vvedite chisla:")
    line = input()
    numbers = parse_numbers(line)
    unique = unique_preserve_order(numbers)
    if not unique:
        print("Otvet: net chisel")
    else:
        print("Otvet:", ' '.join(fmt(n) for n in unique))
