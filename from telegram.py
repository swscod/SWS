from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import Update

# Replace 'YOUR_TOKEN' with the token you received from BotFather
TOKEN = 'AAGLta0M7V1_w_awSskSOme41MS39iOqDBU'

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="مرحباً، أهلاً بك في بوت التواصل!")

def echo(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def info(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="هذا بوت بسيط يرد على بعض الأوامر!")

def help_command(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="يمكنك استخدام /start لبدء البوت و /info للحصول على معلومات!")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))
dispatcher.add_handler(CommandHandler('info', info))
dispatcher.add_handler(CommandHandler('help', help_command))

updater.start_polling()
updater.idle()