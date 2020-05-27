import telebot
import config
import utils
from telebot import types


bot = telebot.TeleBot(config.TOKEN)

meetupOnGoing = True
markupkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
inlinekeyboard = types.InlineKeyboardMarkup()

inButtontest = types.InlineKeyboardButton(text="Начать тест",
                                          callback_data="test")

ButtonLeaders = types.KeyboardButton("Таблица лидеров")
ButtonFAQ = types.KeyboardButton("FAQ")

if meetupOnGoing is True:
    markupkeyboard.add(ButtonLeaders)
    inlinekeyboard.add(inButtontest)

markupkeyboard.add(ButtonFAQ)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, config.WELCOMETEXT,
                     parse_mode='html',
                     reply_markup=markupkeyboard)

    if meetupOnGoing is True:
        bot.send_message(message.chat.id, "Поиграем?",
                         parse_mode='html',
                         reply_markup=inlinekeyboard)


@bot.message_handler(commands=['help'])
def help(message):
    utils.show_help()


@bot.message_handler(content_types=['text'])
def anytext(message):
    s = message.text
    if s == ButtonFAQ.text:
        utils.show_faq()

    elif s == ButtonLeaders.text:
        utils.show_leaders()

    else:
        bot.send_message(message.chat.id, config.DONTUNDERSTAND,
                         parse_mode='html',
                         reply_markup=markupkeyboard)


bot.infinity_polling(True)
