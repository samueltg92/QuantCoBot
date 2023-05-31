from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import Updater
import time

TOKEN_DEL_BOT = "5963451255:AAGPxyC1fAWr_m-rugp5332ljeGN8HPL_hU"
ID_DEL_CHAT = "-1001621135988"
ID_DEL_CANAL = "-1001938210460"

def handle_message(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.chat_id == ID_DEL_CHAT:
        context.bot.forward_message(chat_id=ID_DEL_CANAL, from_chat_id=ID_DEL_CHAT, message_id=message.message_id)

def main():
    bot = Bot(token=TOKEN_DEL_BOT)
    updater = Updater(token=TOKEN_DEL_BOT, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, handle_message))

    updater.start_polling(poll_interval=60.0)
    updater.idle()

if __name__ == "__main__":
    main()
