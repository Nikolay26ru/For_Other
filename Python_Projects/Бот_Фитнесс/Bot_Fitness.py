import telebot
import requests

# Создание экземпляра бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот @FitnessBot. Чем я могу помочь тебе сегодня?')

# Обработчик команды /exercise
@bot.message_handler(commands=['exercise'])
def get_exercise(message):
    # Получение случайного упражнения с помощью API
    response = requests.get('https://api.example.com/exercises')
    data = response.json()
    exercise = data['exercise']

    # Отправка пользователю случайного упражнения
    bot.reply_to(message, f'Сегодняшнее упражнение: {exercise}')

# Обработчик команды /workout
@bot.message_handler(commands=['workout'])
def get_workout(message):
    # Получение случайной тренировки с помощью API
    response = requests.get('https://api.example.com/workouts')
    data = response.json()
    workout = data['workout']

    # Отправка пользователю случайной тренировки
    bot.reply_to(message, f'Сегодняшняя тренировка: {workout}')

# Обработчик команды /nutrition
@bot.message_handler(commands=['nutrition'])
def get_nutrition(message):
    # Получение совета по питанию с помощью API
    response = requests.get('https://api.example.com/nutrition')
    data = response.json()
    nutrition_tip = data['nutrition_tip']

    # Отправка пользователю совета по питанию
    bot.reply_to(message, f'Совет по питанию: {nutrition_tip}')

# Обработчик команды /motivation
@bot.message_handler(commands=['motivation'])
def get_motivation(message):
    # Получение мотивационного сообщения с помощью API
    response = requests.get('https://api.example.com/motivation')
    data = response.json()
    motivation_message = data['motivation_message']

    # Отправка пользователю мотивационного сообщения
    bot.reply_to(message, f'Мотивационное сообщение: {motivation_message}')

# Запуск бота
bot.polling()
