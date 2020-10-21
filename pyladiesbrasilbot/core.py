from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN
from utils.messages import (
    HELLO_MESSAGE,
    HELP_MESSAGE,
    START_MESSAGE,
    WELCOME_NEW_MEMBER_MESSAGE,
)


def start(update, context):
    response_message = START_MESSAGE
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def help(update, context):
    message = HELP_MESSAGE
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def welcome(update, context):
    for new_member in update.message.new_chat_members:
        chat_title = update.message.chat.title

        if not new_member.is_bot:
            first_name = new_member.first_name
            last_name = new_member.last_name
            username = new_member.username

            if last_name is None:
                last_name = ""

            message = WELCOME_NEW_MEMBER_MESSAGE.format(
                first_name=first_name,
                last_name=last_name,
                username=username,
                chat_title=chat_title,
            )
            context.bot.sendPhoto(
                chat_id=update.effective_chat.id,
                photo=open("pyladiesbrasilbot/utils/welcome_pyladies_recife.jpg", "rb"),
                caption=message,
            )
        elif new_member.full_name == "PyLadies Brasil Bot":
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=HELLO_MESSAGE.format(chat_title=chat_title),
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
