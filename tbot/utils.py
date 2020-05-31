from config import FIRST_X_LEADERS, DB_DIR, bot, QUESTIONS_AMOUNT
import sqlite3 as sqlite
from datetime import date, datetime
from telebot import types


meetings = []


def show_faq(chat_id):
    bot.send_message(chat_id, "Отвечаю",
                     parse_mode='html')


def show_leaders(chat_id):
    try:
        db = None
        db = sqlite.connect(DB_DIR)
    except Exception:
        print ("Database can't be opened")
        return -1

    cursor = db.cursor()
    sql = "SELECT telegram_id, tests_score, competition_score FROM peopleandmeetings_person ORDER BY competition_score DESC LIMIT {}".format(FIRST_X_LEADERS)
    cursor.execute(sql)
    a = cursor.fetchone()
    f = 'Таблица лидеров\n'
    while a is not None:
        f = f + a[0] + ' ' + str(a[1]) + ' ' + str(a[2]) + '\n'
        a = cursor.fetchone()
    bot.send_message(chat_id, f, parse_mode='html')
    db.close()


def show_help(chat_id):
    bot.send_message(chat_id, "Помогаю",
                     parse_mode='html')


def start_test(message):
    try:
        db = None
        db = sqlite.connect(DB_DIR)
    except Exception:
        print ("Database can't be opened")
        return -1
    cursor = db.cursor()

    telegram_id = message.from_user.username
    tests_score = 0
    competition_score = 0

    # Проверка на существование человека в базе данных и добавление
    sql = "SELECT telegram_id FROM peopleandmeetings_person WHERE telegram_id = '@{}'".format(telegram_id)
    cursor.execute(sql)
    a = cursor.fetchall()
    if not a:
        sql = "INSERT INTO peopleandmeetings_person (telegram_id, tests_score, competition_score) VALUES ('@{}', {}, {})".format(telegram_id, tests_score, competition_score)
        cursor.execute(sql)
        db.commit()

    tod = str(date.today())
    sql = "SELECT meeting_name FROM peopleandmeetings_meeting WHERE date = '{}'".format(tod)
    cursor.execute(sql)
    a = cursor.fetchall()
    if len(a) > 1:
        inlinekeyboard = types.InlineKeyboardMarkup()
        buttons = []
        for i in range(0, len(a)):
            meetings.append(a[i][0])
            buttons.append(types.InlineKeyboardButton(text=a[i][0],
                                           callback_data="{}".format(a[i][0])))
            inlinekeyboard.add(buttons[i])
        bot.send_message(message.chat.id, "На каком вы мероприятии?",
                         parse_mode='html', reply_markup=inlinekeyboard, show_alert=True)
    else:
        sql = "SELECT id FROM peopleandmeetings_person WHERE telegram_id = '@{}'".format(telegram_id)
        cursor.execute(sql)
        person_id = cursor.fetchone()
        meeting_name = a[0][0]
        sql = "SELECT id FROM peopleandmeetings_meeting WHERE meeting_name = '{}'".format(meeting_name)
        cursor.execute(sql)
        meeting_id = cursor.fetchone()
        sql = "INSERT INTO peopleandmeetings_person_visited_meetings (person_id, meeting_id) VALUES({},{})".format(person_id, meeting_id)


    sql = "SELECT tests_question.* FROM tests_question, tests_category WHERE (tests_question.category_id = tests_category.id) AND (tests_category.isOn = True) AND (tests_question.difficulty = 'Medium' OR tests_question.difficulty = 'Hard') ORDER BY RANDOM() LIMIT {}".format(QUESTIONS_AMOUNT)

    db.close()

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    for i in range(0, len(meetings)):
        if call.data == '{}'.format(meetings[i]):
            pass



            sql = "SELECT id FROM peopleandmeetings_meeting WHERE meeting_name = '{}'".format(meetings[i])
            cursor.execute(sql)
            meeting_id = cursor.fetchone()
            sql = "INSERT INTO peopleandmeetings_person_visited_meetings (person_id, meeting_id) VALUES({},{})".format(person_id, meeting_id)
