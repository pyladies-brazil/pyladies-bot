import pickle

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN
from utils import load_file
from utils.constants import DEFAULT_PHOTO_WELCOME, DEFAULT_PICKEL_FILE
from utils.messages import (
    CONF_BOAS_VINDAS_PHOTO_INFO_CHECK,
    CONF_BOAS_VINDAS_PHOTO_INFO,
    HELLO_MESSAGE,
    HELP_MESSAGE,
    START_MESSAGE,
    UNKNOWN_MESSAGE,
    WELCOME_NEW_MEMBER_MESSAGE,
)


def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("imagem_boas_vindas", imagem_boas_vindas))
    dispatcher.add_handler(CommandHandler("boas_vindas_foto", boas_vindas_foto_info))
    dispatcher.add_handler(
        MessageHandler(
            filters=Filters.photo
            & (
                Filters.caption(
                    [
                        "/boas_vindas_foto",
                        "/boas_vindas_foto@PyLadiesBrasilBot",
                    ]
                )
            ),
            callback=boas_vindas_foto,
        )
    )
    dispatcher.add_handler(CommandHandler("boas_vindas", boas_vindas))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(
        MessageHandler(Filters.status_update.new_chat_members, welcome)
    )
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


def start(update, context):
    response_message = START_MESSAGE
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MESSAGE)


def imagem_boas_vindas(update, context):
    chat_id = update.effective_chat.id

    context.bot.sendPhoto(
        chat_id=chat_id,
        photo=load_file(
            context=context,
            pickle_file=DEFAULT_PICKEL_FILE,
            default_photo=DEFAULT_PHOTO_WELCOME,
            chat_id=chat_id,
        ),
    )


def boas_vindas_foto_info(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=CONF_BOAS_VINDAS_PHOTO_INFO,
    )


def boas_vindas_foto(update, context):
    photos = update.message.photo
    if photos:
        photo_id = photos[-1].file_id
        chat_id = update.effective_chat.id

        dict_photo = {chat_id: photo_id}

        with open(DEFAULT_PICKEL_FILE, "ab") as files:
            pickle.dump(dict_photo, files, protocol=pickle.HIGHEST_PROTOCOL)

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=CONF_BOAS_VINDAS_PHOTO_INFO_CHECK,
        )


def boas_vindas(update, context):
    pass


def welcome(update, context):
    chat_id = update.effective_chat.id

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
                chat_id=chat_id,
                photo=load_file(
                    context=context,
                    pickle_file=DEFAULT_PICKEL_FILE,
                    default_photo=DEFAULT_PHOTO_WELCOME,
                    chat_id=chat_id,
                ),
                caption=message,
            )
        elif new_member.full_name == "PyLadies Brasil Bot":
            context.bot.send_message(
                chat_id=chat_id,
                text=HELLO_MESSAGE.format(chat_title=chat_title),
            )


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=UNKNOWN_MESSAGE,
    )


if __name__ == "__main__":
    print("press CTRL + C to cancel.")
    main()
