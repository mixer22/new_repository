import telebot
import datetime

bot = telebot.TeleBot("1316919471:AAHNv3rQi6YRpTVC-u36QG9BgHZg-y6dT1w")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", callback_data='good')
    keyboard.add(url_button, url_button)
    # keyboard.add(url_button)
    print(message)
    print(datetime.datetime.fromtimestamp(message.date))
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик. \U000026C4", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    print(call)

if __name__ == '__main__':
    bot.polling()

     