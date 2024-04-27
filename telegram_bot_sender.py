import sys
sys.dont_write_bytecode = True


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot
from config import token, chat_id
import os
import threading as t

def threading_func(*app):
    """ threading to open apps """

    print("Thread name -> {}".format(t.current_thread().name))
    print(f"app name -> {app[0]}")
    os.system(app[0])

class tele_bot():

    def __init__(self):
        """init function"""

        self.bot_token = token
        self.chat_id = chat_id
        self.bot = Bot(self.bot_token)
        self.updater = Updater(self.bot_token, use_context=True)

    def start(self, update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('Hi!')

    def echo(self, update, context):
        """Echo the user message."""
        d = update["message"]["text"]
        print(d)

        if d[0] == r"/":
            d = d.replace("/", "")
            thread =  t.Thread(target = threading_func, args=(d,))
            thread.start()
        else:
            update.message.reply_text(update.message.text)



    def sen(self, message):
        """For sending message."""
        self.bot.sendMessage(chat_id=self.chat_id, text=message)

    def dispatch(self):
        self.dp = self.updater.dispatcher

    def handles(self):
        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(MessageHandler(Filters.text, self.echo))

    def main(self):
        """Start the bot."""
        self.dispatch()
        self.handles()
        self.updater.start_polling()
        self.updater.idle()


# if __name__ == '__main__':
#     # x = tele_bot()
#     # x.sen("niknk")
#     # x.main()
#     print("HI")