import pickle
from io import BytesIO


def load_pickle(pickle_file):
    try:
        with open(pickle_file, "rb") as files:
            dict = pickle.load(files)
    except FileNotFoundError:
        dict = {}

    return dict


def load_file(context, pickle_file, default_photo, chat_id):
    dict_files = load_pickle(pickle_file)

    photo_id = dict_files.get(chat_id)

    if photo_id is None:
        photo = open(default_photo, "rb")
    else:
        file = context.bot.get_file(photo_id)
        photo = BytesIO(file.download_as_bytearray())

    return photo


def save_pickle(pickle_file, dict):
    old_dict = load_pickle(pickle_file)
    old_dict.update(dict)

    with open(pickle_file, "wb") as files:
        pickle.dump(old_dict, files, protocol=pickle.HIGHEST_PROTOCOL)
