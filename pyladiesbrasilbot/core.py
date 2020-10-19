from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN


def start(update, context):
    response_message = "=^._.^="
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def http_cats(update, context):
    context.bot.sendPhoto(
        chat_id=update.effective_chat.id, photo=BASE_API_URL + context.args[0]
    )


def unknown(update, context):
    response_message = "Meow? =^._.^="
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("http", http_cats, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.all, unknown))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    print("press CTRL + C to cancel.")
    main()
