import telebot
from datetime import datetime

# Создание экземпляра бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Словарь для хранения задач пользователей
tasks = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот-органайзер. Чем могу помочь?')

# Обработчик команды /newtask
@bot.message_handler(commands=['newtask'])
def new_task(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Введите описание задачи:')
    bot.register_next_step_handler(message, save_task)

def save_task(message):
    chat_id = message.chat.id
    task_description = message.text
    tasks[chat_id] = task_description
    bot.reply_to(message, 'Задача сохранена.')

# Обработчик команды /tasks
@bot.message_handler(commands=['tasks'])
def show_tasks(message):
    chat_id = message.chat.id
    if chat_id in tasks:
        task_description = tasks[chat_id]
        bot.reply_to(message, f'Ваша задача: {task_description}')
    else:
        bot.reply_to(message, 'У вас нет задач.')

# Обработчик команды /reminder
@bot.message_handler(commands=['reminder'])
def set_reminder(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Введите дату и время напоминания в формате ДД-ММ-ГГГГ ЧЧ:ММ:')
    bot.register_next_step_handler(message, save_reminder)

def save_reminder(message):
    chat_id = message.chat.id
    reminder_datetime = datetime.strptime(message.text, '%d-%m-%Y %H:%M')
    now = datetime.now()
    time_difference = reminder_datetime - now
    seconds = time_difference.total_seconds()
    if seconds > 0:
        bot.reply_to(message, f'Напоминание установлено на {reminder_datetime}.')
        bot.send_message(chat_id, 'Напоминание: Пора выполнить задачу!')
    else:
        bot.reply_to(message, 'Некорректная дата и время. Попробуйте еще раз.')

# Запуск бота
bot.polling()
