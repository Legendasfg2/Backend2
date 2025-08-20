import telebot

# Вставь сюда токен, который дал BotFather
TOKEN = "7545290164:AAEYBAne-juetj-YKtxL9sw2S2dvzB00pwE"

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет 👋! Я твой первый Telegram-бот!")

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

# Запуск бота
bot.polling()
