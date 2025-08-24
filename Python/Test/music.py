import json
import random
import os
import pygame

PLAYLIST_FILE = "playlist.json"

# Загружаем плейлист
def load_playlist():
    if os.path.exists(PLAYLIST_FILE):
        with open(PLAYLIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Сохраняем плейлист
def save_playlist(playlist):
    with open(PLAYLIST_FILE, "w", encoding="utf-8") as f:
        json.dump(playlist, f, ensure_ascii=False, indent=4)

# Добавление песни
def add_song():
    title = input("Название песни: ")
    artist = input("Исполнитель: ")
    path = input("Укажи путь к файлу (mp3 или wav): ")

    if not os.path.exists(path):
        print("❌ Файл не найден!")
        return

    song = {"title": title, "artist": artist, "path": path}
    playlist.append(song)
    save_playlist(playlist)
    print(f"✅ Песня '{title}' добавлена!")

# Запуск песни
def play_song(song):
    print(f"▶ Сейчас играет: {song['title']} — {song['artist']}")
    pygame.mixer.init()
    pygame.mixer.music.load(song["path"])
    pygame.mixer.music.play()

# Плеер с управлением
def player():
    if not playlist:
        print("Плейлист пуст!")
        return

    current_song = random.choice(playlist)
    play_song(current_song)

    while True:
        print("\n--- Управление ---")
        print("⏸ (p) Пауза")
        print("▶ (r) Продолжить")
        print("⏭ (n) Следующая песня")
        print("⏹ (s) Стоп и выход")
        cmd = input(">>> ").lower()

        if cmd == "p":  # пауза
            pygame.mixer.music.pause()
            print("⏸ Пауза")
        elif cmd == "r":  # продолжить
            pygame.mixer.music.unpause()
            print("▶ Продолжение")
        elif cmd == "n":  # следующая песня
            current_song = random.choice(playlist)
            play_song(current_song)
        elif cmd == "s":  # стоп
            pygame.mixer.music.stop()
            print("⏹ Остановлено")
            break
        else:
            print("Неизвестная команда!")

# Главное меню
def menu():
    while True:
        print("\n🎵 Музыкальный плейлист")
        print("1. Добавить песню")
        print("2. Запустить плеер")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_song()
        elif choice == "2":
            player()
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор!")

playlist = load_playlist()
menu()
