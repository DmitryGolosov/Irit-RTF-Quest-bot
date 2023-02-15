import telebot
from telebot import types

from time import sleep
from clients import config
from app import quest
from app.responseData import ResponseData
from app.database.usersDatabase import UsersData

bot = telebot.TeleBot(config.bot_token)
users = UsersData()


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_keyboard(items: list[str]):
    pent = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        pent.add(types.KeyboardButton(item))
    return pent


def send_messages(data: list[ResponseData]):
    for message in data:
        if message.has_image:
            caption = None
            if message.has_text:
                caption = message.text
            if len(message.images_path) == 1:
                bot.send_photo(message.user_id, open(message.images_path[0], "rb"), caption=caption)
            if len(message.images_path) > 1:
                images = [telebot.types.InputMediaPhoto(open(path, "rb")) for path in message.images_path]
                bot.send_media_group(message.user_id, images, caption=caption)
            continue

        keyboard = get_remove_markup()
        if message.has_keyboard:
            keyboard = get_keyboard(message.keyboard_items)
        if message.do_not_change_keyboard:
            keyboard = None

        if message.has_text:
            bot.send_message(message.user_id, message.text, reply_markup=keyboard)
            sleep(0.08)


@bot.message_handler(commands=['start'])
def on_start(message):
    send_messages([quest.start(message.chat.id, users)])


@bot.message_handler(commands=['stop'])
def on_stop(message):
    send_messages([quest.stop(message.chat.id, users)])


@bot.message_handler(content_types=['text'])
def main_story(message):
    if message.text == config.stop_passwd:
        raise Exception("Bot stopped by stop passwd")
    send_messages(quest.main_story(message.chat.id, message.text, users))


def run(users_db: UsersData):
    global users
    users = users_db
    try:
        print("Запуск тг бота")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Хьюстон, у тг большие проблемы\n{e}")
