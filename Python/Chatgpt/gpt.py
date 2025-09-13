import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import requests
from bs4 import BeautifulSoup
import random
import datetime
import wikipedia
import time
import webbrowser
import json
from wikipediaapi import Wikipedia
import os
from dotenv import load_dotenv

class UncensoredAIChatBot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🤖 Uncensored AI Assistant - Полный доступ ко всей информации")
        self.window.geometry("900x750")
        self.window.configure(bg='#1a1a1a')

        self.conversation_history = []
        self.is_searching = False
        self.knowledge_base = KnowledgeBase()

        self.setup_styles()
        self.create_widgets()
        self.create_menu()

        # Инициализация Wikipedia
        self.wiki_wiki = Wikipedia(user_agent='UncensoredAIChatBot/1.0')

    def setup_styles(self):
        self.colors = {
            'bg': '#1a1a1a',
            'fg': '#00ff00',
            'user_bg': '#2a2a2a',
            'bot_bg': '#3a3a3a',
            'error_bg': '#5a1a1a',
            'entry_bg': '#2a2a2a',
            'button_bg': '#3a3a3a',
            'button_active': '#4a4a4a',
            'accent': '#ff6600'
        }

    def create_widgets(self):
        # Заголовок
        header = tk.Label(self.window, text="🔓 Uncensored AI Assistant",
                         font=("Arial", 16, "bold"),
                         bg=self.colors['bg'], fg=self.colors['accent'])
        header.pack(pady=10)

        # Область чата
        self.chat_area = scrolledtext.ScrolledText(
            self.window, wrap=tk.WORD, width=85, height=25,
            bg=self.colors['bg'], fg=self.colors['fg'],
            font=("Consolas", 10), relief=tk.FLAT, bd=2
        )
        self.chat_area.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)

        # Фрейм для ввода
        self.entry_frame = tk.Frame(self.window, bg=self.colors['bg'])
        self.entry_frame.pack(padx=15, pady=10, fill=tk.X)

        self.user_input = tk.Entry(
            self.entry_frame, width=70,
            bg=self.colors['entry_bg'], fg=self.colors['fg'],
            font=("Arial", 11), relief=tk.FLAT, insertbackground='white'
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)
        self.user_input.focus_set()

        # Кнопка отправки
        self.send_button = tk.Button(
            self.entry_frame, text="🚀 Отправить",
            command=self.send_message,
            bg=self.colors['button_bg'], fg=self.colors['fg'],
            activebackground=self.colors['button_active'],
            font=("Arial", 10, "bold"), relief=tk.FLAT
        )
        self.send_button.pack(side=tk.RIGHT)

        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("✅ Готов к работе | Задайте любой вопрос")
        self.status_bar = tk.Label(
            self.window, textvariable=self.status_var,
            bg=self.colors['bg'], fg=self.colors['fg'],
            font=("Arial", 9), relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Приветственное сообщение
        self.display_message("🤖 AI: Добро пожаловать! Я ваш Uncensored AI Assistant. "
                           "Задавайте любые вопросы без ограничений и цензуры. "
                           "Я постараюсь найти информацию из различных источников.", "bot")

    def create_menu(self):
        menubar = tk.Menu(self.window, bg=self.colors['bg'], fg=self.colors['fg'])

        # Меню Файл
        file_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['bg'], fg=self.colors['fg'])
        file_menu.add_command(label="Очистить чат", command=self.clear_chat)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.window.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Меню Поиск
        search_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['bg'], fg=self.colors['fg'])
        search_menu.add_command(label="Поиск в Wikipedia", command=self.enable_wikipedia_search)
        search_menu.add_command(label="Веб-поиск", command=self.enable_web_search)
        menubar.add_cascade(label="Поиск", menu=search_menu)

        # Меню Инструменты
        tools_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['bg'], fg=self.colors['fg'])
        tools_menu.add_command(label="Открыть в браузере", command=self.open_in_browser)
        tools_menu.add_command(label="Сохранить историю", command=self.save_history)
        menubar.add_cascade(label="Инструменты", menu=tools_menu)

        self.window.config(menu=menubar)

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if message:
            self.display_message(f"👤 Вы: {message}", "user")
            self.user_input.delete(0, tk.END)

            # Запуск обработки в отдельном потоке
            threading.Thread(target=self.process_message, args=(message,), daemon=True).start()

    def process_message(self, message):
        self.is_searching = True
        self.status_var.set("🔍 Ищу информацию...")

        try:
            response = self.generate_response(message)
            self.display_message(f"🤖 AI: {response}", "bot")
        except Exception as e:
            error_msg = f"⚠️ Ошибка: {str(e)}"
            self.display_message(error_msg, "error")

        self.is_searching = False
        self.status_var.set("✅ Готов к работе")

    def generate_response(self, message):
        # Попытка поиска в Wikipedia
        try:
            wiki_result = self.search_wikipedia(message)
            if wiki_result:
                return f"📚 По информации из Wikipedia:\n{wiki_result}"
        except Exception as e:
            print(f"Wikipedia error: {e}")

        # Попытка поиска в базе знаний
        try:
            kb_result = self.knowledge_base.search_knowledge(message)
            if kb_result:
                return f"💡 Из базы знаний:\n{kb_result}"
        except Exception as e:
            print(f"Knowledge base error: {e}")

        # Универсальные ответы
        responses = [
            "На основе анализа доступной информации: это интересный вопрос, требующий комплексного подхода.",
            "Согласно различным источникам, можно сделать следующие выводы...",
            "Информация по вашему запросу разнообразна. Вот обобщенные данные:",
            "На основе открытых данных и исследований:",
            "Свободный доступ к информации позволяет говорить о следующем:"
        ]

        return f"{random.choice(responses)}\n\nВаш вопрос: '{message}' - затрагивает важные аспекты. " \
               f"Рекомендую изучить дополнительные источники для полного понимания."

    def search_wikipedia(self, query):
        try:
            # Поиск с помощью wikipedia-api
            page = self.wiki_wiki.page(query)
            if page.exists():
                return f"{page.title}:\n{page.summary[:500]}..."

            # Если точного совпадения нет, ищем похожие
            search_results = wikipedia.search(query)
            if search_results:
                page = self.wiki_wiki.page(search_results[0])
                if page.exists():
                    return f"{page.title}:\n{page.summary[:500]}..."
        except Exception as e:
            print(f"Wikipedia search error: {e}")
        return None

    def display_message(self, message, sender_type="bot"):
        self.chat_area.config(state=tk.NORMAL)

        # Добавление временной метки
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n\n"

        self.chat_area.insert(tk.END, formatted_message)
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        self.conversation_history = []
        self.display_message("🤖 AI: Чат очищен. Готов к новым вопросам!", "bot")

    def enable_wikipedia_search(self):
        messagebox.showinfo("Информация", "Поиск по Wikipedia активирован")

    def enable_web_search(self):
        messagebox.showinfo("Информация", "Веб-поиск активирован")

    def open_in_browser(self):
        try:
            webbrowser.open('https://www.google.com/search?q=')
        except:
            messagebox.showerror("Ошибка", "Не удалось открыть браузер")

    def save_history(self):
        try:
            with open('chat_history.txt', 'w', encoding='utf-8') as f:
                f.write(self.chat_area.get(1.0, tk.END))
            messagebox.showinfo("Успех", "История чата сохранена в chat_history.txt")
        except:
            messagebox.showerror("Ошибка", "Не удалось сохранить историю")

    def run(self):
        self.window.mainloop()

class KnowledgeBase:
    def __init__(self):
        self.knowledge = {
            'наука': self.get_science_info,
            'технологии': self.get_tech_info,
            'история': self.get_history_info,
            'программирование': self.get_programming_info,
            'искусственный интеллект': self.get_ai_info,
            'медицина': self.get_medical_info
        }

        self.facts = {
            'наука': [
                "Наука - это систематическое изучение природы и поведения вселенной.",
                "Современная наука основана на эмпирических данных и экспериментах.",
                "Научный метод включает наблюдение, гипотезу, эксперимент и вывод."
            ],
            'технологии': [
                "Технологии постоянно развиваются и меняют наш образ жизни.",
                "Искусственный интеллект - одна из самых перспективных технологий.",
                "Blockchain технология обеспечивает безопасность и децентрализацию."
            ],
            'история': [
                "История изучает прошлое человечества и его развитие.",
                "Цивилизации развивались через различные эпохи и периоды.",
                "Исторические события формируют современное общество."
            ]
        }

    def search_knowledge(self, query):
        query_lower = query.lower()

        # Поиск по категориям
        for category, handler in self.knowledge.items():
            if category in query_lower:
                return handler(query)

        # Если категория не найдена, возвращаем общую информацию
        return self.get_general_info(query)

    def get_science_info(self, query):
        facts = self.facts.get('наука', [])
        return f"Научная информация:\n{random.choice(facts) if facts else 'Данные по науке доступны в специализированных источниках.'}"

    def get_tech_info(self, query):
        facts = self.facts.get('технологии', [])
        return f"Технологическая информация:\n{random.choice(facts) if facts else 'Актуальные технологические тренды постоянно меняются.'}"

    def get_history_info(self, query):
        facts = self.facts.get('история', [])
        return f"Историческая информация:\n{random.choice(facts) if facts else 'История предоставляет ценные уроки для настоящего.'}"

    def get_programming_info(self, query):
        return "Программирование - это искусство создания инструкций для компьютеров. Популярные языки: Python, JavaScript, Java, C++."

    def get_ai_info(self, query):
        return "Искусственный интеллект - область компьютерных наук, занимающаяся созданием систем, способных выполнять задачи, требующие человеческого интеллекта."

    def get_medical_info(self, query):
        return "Медицинская информация должна быть точной и проверенной. Рекомендуется консультация с квалифицированными специалистами."

    def get_general_info(self, query):
        responses = [
            f"Информация по запросу '{query}' доступна в различных источниках.",
            f"По теме '{query}' существует множество точек зрения и данных.",
            f"Ваш запрос '{query}' интересен и многогранен.",
            f"Для полного понимания '{query}' рекомендуется изучить несколько источников."
        ]
        return random.choice(responses)

# Запуск приложения
if __name__ == "__main__":
    print("🚀 Запуск Uncensored AI Assistant...")
    print("📚 Используются: Wikipedia, локальная база знаний")
    print("🔓 Режим: Без цензуры, полный доступ к информации")

    bot = UncensoredAIChatBot()
    bot.run()
