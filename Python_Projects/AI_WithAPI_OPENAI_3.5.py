import telebot
import tensorflow as tf
import openai
# Загрузка API-ключа для OpenAI ChatGPT
openai.api_key = 'YOUR_OPENAI_API_KEY'
# Создание экземпляра телеграм-бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот с нейросетью. Чем могу помочь?')
# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def process_message(message):
    # Получение текста сообщения от пользователя
    text = message.text
    # Генерация ответа с помощью ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    # Извлечение ответа из ответа ChatGPT
    reply = response.choices[0].text.strip()
    # Отправка ответа пользователю
    bot.reply_to(message, reply)
# Запуск бота
bot.polling()
