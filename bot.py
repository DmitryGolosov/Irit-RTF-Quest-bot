#!/usr/bin/python
# -*- coding: utf8 -*-
import telebot
import config
from telebot import types
from branches.firstBranch import firstBranch
from branches.secondBranch import secondBranch
from branches.thirdBranch import thirdBranch
from database.usersDatabase import UsersData
from database import usersDispatcher

bot = telebot.TeleBot(config.bot_token)
users = UsersData()


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_main_keyboard():
    pent = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Студотряды")
    item2 = types.KeyboardButton("Традиции ИРИТ-РТФ")
    item3 = types.KeyboardButton("Известные выпускники ИРИТ-РТФ")
    pent.add(item1)
    pent.add(item2)
    pent.add(item3)
    return pent


def get_start_keyboard():
    start = types.ReplyKeyboardMarkup(resize_keyboard
                                      =True)
    item = types.KeyboardButton("Поехали")
    start.add(item)
    return start

@bot.message_handler(commands=['start'])
def on_start(message):
    users.add_user(message.chat.id)
    bot.send_message(message.chat.id, 'Привет!')
    bot.send_message(message.chat.id, "Это создатели данного квеста и мы предлагаем тебе ознакомиться с его "
                                      "содержанием. Если ты хочешь узнать традиции ИРИТ-РТФ, историю студотрядов или "
                                      "известных людей, которые закончили ИРИТ-РТФ, то нажимай кнопку ПОЕХАЛИ и начнем "
                                      "наше приключение!\nДля остановки бота введите /stop",
                     reply_markup=get_start_keyboard())


@bot.message_handler(commands=['stop'])
def on_stop(message):
    users.remove_user(message.chat.id)
    bot.send_message(message.chat.id, "Бот успешно отключен.\nДля начала работы введите /start", reply_markup=get_remove_markup())


@bot.message_handler(content_types=['text'])
def main_story(message):
    if not users.contains(message.chat.id):
        bot.send_message(message.chat.id, "Неправильное начало диалога. Воспитанные люди сначала пишут /start")
        return

    if message.text == 'Поехали':
        bot.send_message(message.chat.id, 'С чего ты хотел(-а) бы начать?',
                         reply_markup=get_main_keyboard())
        return
    if message.text == 'Студотряды'\
            or users.get_branch(message.chat.id) == 1:
        firstBranch.run(message, users, bot, on_start)
        return
    if message.text == 'Традиции ИРИТ-РТФ' \
            or users.get_branch(message.chat.id) == 2:
        secondBranch.run(message, users, bot, on_start)
        return
    if message.text == 'Известные выпускники ИРИТ-РТФ' \
            or users.get_branch(message.chat.id) == 3:
        thirdBranch.run(message, users, bot, on_start)
        return

    bot.send_message(message.chat.id, "Команда не реализована")


if __name__ == '__main__':
    user_data_filename = "database/usersData.json"
    try:
        users = usersDispatcher.try_load_users_info_from_json(user_data_filename)
        print("Запуск бота")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Хьюстон, у нас большие проблемы\n{e}")
    finally:
        usersDispatcher.save_users_info(user_data_filename, users)
        print("Данные сохранены")
