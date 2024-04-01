import telebot
from googletrans import Translator

# Создание экземпляра бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Создание экземпляра переводчика
translator = Translator(service_urls=['translate.google.com'])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот-переводчик. Отправь мне текст на одном языке, и я переведу его на другой язык.')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        # Получение текста сообщения
        text = message.text

        # Определение языка и перевод текста
        translation = translator.translate(text, dest='en')

        # Отправка перевода пользователю
        bot.reply_to(message, f'Перевод: {translation.text}')
    except Exception as e:
        bot.reply_to(message, 'Произошла ошибка при переводе текста.')

# Запуск бота
bot.polling()
