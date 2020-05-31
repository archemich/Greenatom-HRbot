from telebot import apihelper
import telebot

# Bot token
TOKEN = '1223276408:AAGcuXPkeJ2NKtp29FX8y0itiwJiv6WxqAA'
bot = telebot.TeleBot(TOKEN)

# Bot behavior settings
FIRST_X_LEADERS = 5
QUESTIONS_AMOUNT = 10

# Proxy settings
ip = '185.161.211.25'
port = '1080'
apihelper.proxy = {
    'https': 'socks5://{}:{}'.format(ip, port)
}


meetupOnGoing = True


# Strings
WELCOMETEXT = 'Здравствуйте, я чат-бот Greenatom'
DONTUNDERSTAND = 'Я всего лишь бот, я такого не понимаю!'


# Database
DB_DIR = "../db.sqlite3"
