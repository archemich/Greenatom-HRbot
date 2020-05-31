from telebot import apihelper
import telebot


# Bot token
TOKEN = '1223276408:AAGcuXPkeJ2NKtp29FX8y0itiwJiv6WxqAA'
bot = telebot.TeleBot(TOKEN)


# Proxy settings
ip = '85.97.176.245'
port = '4145'
apihelper.proxy = {
    'https': 'socks5://{}:{}'.format(ip, port)
}


meetupOnGoing = True


# Strings
WELCOMETEXT = 'Здравствуйте, я чат-бот Greenatom'
DONTUNDERSTAND = 'Я всего лишь бот, я такого не понимаю!'


# Database
FIRSTXLEADERS = 5