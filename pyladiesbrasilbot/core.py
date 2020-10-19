from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN


def start(update, context):
    response_message = (
        "Olá, eu sou a PyLadies Brasil Bot! "
        "Ainda estou em construção, mas espero poder te ajudar."
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def help(update, context):
    message = "Lista de comandos ainda em construção..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def welcome(update, context):
    for new_member in update.message.new_chat_members:
        if not new_member.is_bot:
            message = (
                f"Seja bem vinda, {new_member.first_name} "
                f"{new_member.last_name} "
                f"(@{new_member.username}) ao {update.message.chat.title}!"
            )
            context.bot.sendPhoto(
                chat_id=update.effective_chat.id,
                photo=open("pyladiesbrasilbot/utils/welcome_pyladies_recife.jpg", "rb"),
                caption=message,
            )


def unknown(update, context):
    response_message = "Comando inválido! Insira /help para ver a lista de comandos"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(
        MessageHandler(Filters.status_update.new_chat_members, welcome)
    )
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    print("press CTRL + C to cancel.")
    main()
