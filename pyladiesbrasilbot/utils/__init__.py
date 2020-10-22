import pickle
from io import BytesIO


def load_file(context, pickle_file, default_photo, chat_id):
    try:
        with open(pickle_file, "rb") as files:
            dict_files = pickle.load(files)
            photo_id = dict_files.get(chat_id)

            if photo_id is None:
                photo = open(default_photo, "rb")
            else:
                file = context.bot.get_file(photo_id)
                photo = BytesIO(file.download_as_bytearray())
    except FileNotFoundError:
        photo = open(default_photo, "rb")

    return photo
