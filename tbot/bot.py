import config
import utils
from telebot import types


bot = config.bot
m = None  # don't delete
isTestPassed = False

meetupOnGoing = config.meetupOnGoing
markupkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
inlinekeyboard = types.InlineKeyboardMarkup()

inButtontest = types.InlineKeyboardButton(text="Начать тест",
                                          callback_data='tst')

ButtonLeaders = types.KeyboardButton("Таблица лидеров")
ButtonFAQ = types.KeyboardButton("FAQ")

if meetupOnGoing is True:
    markupkeyboard.add(ButtonLeaders)
    inlinekeyboard.add(inButtontest)

markupkeyboard.add(ButtonFAQ)


@bot.message_handler(commands=['start'])
def welcome(message):
    global m
    m = message
    bot.send_message(message.chat.id, config.WELCOMETEXT,
                     parse_mode='html',
                     reply_markup=markupkeyboard)

    if meetupOnGoing is True:
        bot.send_message(message.chat.id, "Поиграем?",
                         parse_mode='html',
                         reply_markup=inlinekeyboard)



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == 'test':
        bot.send_message(call.message.chat.id, 'Тпуо',
                         parse_mode='html')
        global isTestPassed
        if not isTestPassed:
            global m
            print(call.from_user.username)
            #utils.start_test(m)
            isTestPassed = True
        else: bot.send_message(call.message.chat.id, "Ты проходил уже тест!",
                             parse_mode='html')



@bot.message_handler(commands=['help'])
def help(message):
    global m
    m = message
    utils.show_help(message.chat.id)


@bot.message_handler(content_types=['text'])
def anytext(message):
    global m
    m = message
    s = message.text
    if s == ButtonFAQ.text:
        utils.show_faq(message.chat.id)

    elif s == ButtonLeaders.text:
        utils.show_leaders(message.chat.id)

    elif s == inButtontest.text:
        if meetupOnGoing is True:
            utils.start_test(message)
        else:
            bot.send_message(message.chat.id, 
                'Никакие мероприятия в данный момент не проводится.', parse_mode='html')

    else:
        bot.send_message(message.chat.id, config.DONTUNDERSTAND,
                         parse_mode='html',
                         reply_markup=markupkeyboard)


if __name__ == '__main__':
    isTestPassed = False
    bot.polling(none_stop=True)
