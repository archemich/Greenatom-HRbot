from telebot import apihelper


TOKEN = '1223276408:AAGcuXPkeJ2NKtp29FX8y0itiwJiv6WxqAA'

ip = '45.91.93.166'
port = '1080'


apihelper.proxy = {
    'https': 'socks5://{}:{}'.format(ip, port)
}


# Strings

WELCOMETEXT = 'Здравствуйте, я чат-бот Greenatom'
DONTUNDERSTAND = 'Я всего лишь бот, я такого не понимаю!'
