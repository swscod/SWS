from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import Update
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