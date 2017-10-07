from telegram.ext import Updater
updater = Updater(token='462381555:AAGpyrfrkxt0_uitj-z4ZFUMDMfQt0MdZhY')

dispatcher = updater.dispatcher
import sqlite3
database_connector = sqlite3.connect
DATABASE = 'sq.sql'
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(bot, update):
    conn = database_connector(DATABASE)
    conn.execute('INSERT INTO Users VALUES (:user_id, :us)', {"user_id": update.message.chat_id, "us": 'User'})
    conn.commit()
    conn.close()
    bot.send_message(chat_id=update.message.chat_id, text="Вы успешно подписались на новости Лисьего Носа!")
    print(update.message.chat_id)

DEBUG = True
def send(bot, update):
    if update.message.chat_id != 130703270:
        return
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM Users')
    for i in cursor.fetchall():
        if DEBUG:
            bot.send_message(chat_id=int(i[0]), text=update.message.text[5:])
        else:
            bot.send_message(chat_id=130703270, text=update.message.text[5:])
    conn.close()
    print('yes')

def kot(bot, update):
    bot.send_message(chat_id=update.message.chat_id, photo=open('test.png', 'rb'))

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('send', send))
dispatcher.add_handler(CommandHandler('kot', kot))

updater.start_polling()
