from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
    print (update.message.from_user.first_name)

f = open('../token.txt')
TOKEN = f.read()
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.start_polling()
updater.idle()


f.close()
