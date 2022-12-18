import telebot
from telebot import types
import os
import random

TOKEN = '5896091526:AAFj9ypjLcmvESOD1Ey41kih3L9caPekX6M'
bot = telebot.TeleBot(TOKEN)
# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("Получить цитату")
    #markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name))
    mes = "Чтобы получить цитату, нажми соответсвующую кнопку"
    bot.send_message(message.chat.id, mes, reply_markup=markup)


quotes = ["Вы живете всего один раз. Не бойтесь быть смешными",
          "Мне наплевать, что вы обо мне думаете. Я о вас не думаю вообще",
          "Моя жизнь не устраивала меня, поэтому я создала свою жизнь",
          "Девушке нужны два качества: она должна быть стильной и потрясающей",
          "Одевайтесь так, как будто сегодня вы собираетесь встретить своего злейшего врага",
          "Так как всё находится в голове, не надо её терять",
          "Если тебе грустно, нанеси немного помады и переходи в наступление",
          "У судьбы нет причин, без причины сводить посторонних",
          "Духи следует наносить туда, куда вы хотите, чтобы мужчина вас поцеловал"
          ]


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text
    if text == "Получить цитату":
        num = random.randint(1, 9) - 1
        image_file = f'images\{num}.jpg'
        img = open(os.path.join(cur_path, image_file), 'rb')
        bot.send_message(message.from_user.id, quotes[num])
        bot.send_photo(message.from_user.id, img)
    else:
        bot.send_message(message.from_user.id, "Нажми кнопку или напиши 'Получить цитату'")


bot.polling(none_stop=True, interval=0)
