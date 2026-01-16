# ...existing code...
import os
import pathlib

# Включаем ANSI-последовательности в Windows (если доступно)
if os.name == "nt":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            kernel32.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    except Exception:
        pass

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Печатаем все строки исходного файла красным
src = pathlib.Path(__file__)
for line in src.read_text(encoding="utf-8").splitlines():
    print(f"{RED}{line}{RESET}")

# Печатаем сам текст зелёным
print(f"{GREEN}Hello{RESET}")
# ...existing code...
