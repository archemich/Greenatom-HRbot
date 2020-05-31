from config import bot
from config import FIRSTXLEADERS
import sqlite3 as sqlite

db = None


def show_faq(chat_id):
    bot.send_message(chat_id, "Отвечаю",
                     parse_mode='html')


def show_leaders(chat_id):
    db = sqlite.connect("../db.sqlite3")
    cursor = db.cursor()
    sql = "SELECT telegram_id, tests_score, competition_score FROM peopleandmeetings_person ORDER BY competition_score DESC LIMIT {}".format(
        FIRSTXLEADERS)
    cursor.execute(sql)

    bot.send_message(chat_id, cursor.fetchall(),
                     parse_mode='html')


def show_help(chat_id):
    bot.send_message(chat_id, "Помогаю",
                     parse_mode='html')


def start_test(chat_id):
    bot.send_message(chat_id, "Начинаю тест",
                     parse_mode='html')
