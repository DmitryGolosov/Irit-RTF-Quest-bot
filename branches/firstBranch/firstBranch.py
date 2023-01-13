import telebot
from telebot import types
from database.usersDatabase import UsersData
from branches.firstBranch import impulsBranch
from branches.firstBranch import astraBranch


def get_remove_markup():
    return types.ReplyKeyboardRemove()


def get_markup_reply():
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("Это трудовой коллектив")
    item4 = types.KeyboardButton("Это коллектив, состоящий из студентов")
    item5 = types.KeyboardButton("Коллектив, деятельность которого происходит во внеучебное время")
    markup_reply.add(item3)
    markup_reply.add(item4)
    markup_reply.add(item5)
    return markup_reply


def get_reply1():
    reply1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item6 = types.KeyboardButton('ССО "Импульс"')
    item7 = types.KeyboardButton('СПО "Астра"')
    item8 = types.KeyboardButton('Никакое')
    reply1.add(item6)
    reply1.add(item7)
    reply1.add(item8)
    return reply1


def run(message, users: UsersData, bot: telebot.TeleBot, to_start):
    users.set_branch(message.chat.id, 1)

    if message.text == 'Студотряды':
        bot.send_message(message.chat.id, 'Осмотреть первый этаж, пройтись по коридору')
        bot.send_message(message.chat.id, 'Ты прогуливался по корпусу и заметил ярко оформленные доски со странными названиями. '
                         '"Студотряд? Что это?" - подумал ты',
                         reply_markup=get_markup_reply())
        return

    if message.text == 'Это трудовой коллектив' \
            or message.text == 'Это коллектив, состоящий из студентов' \
            or message.text == 'Коллектив, деятельность которого происходит во внеучебное время':
        bot.send_photo(message.chat.id, open("Использованные/FirstBranch.jpg", "rb"))
        bot.send_message(message.chat.id,
                         'Разглядывая фотографии улыбающихся ребят и изучая информацию на досках, ты понял, '
                         'что студенческие отряды - это трудовые коллективы, сформированные, в основном, '
                         'из числа обучающихся образовательных организаций высшего образования для совместной работы '
                         'в свободное от учёбы время (как правило, в период летних каникул)',
                         reply_markup=get_remove_markup())
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open("Использованные/FirstBranch2.jpg", "rb")),
                                               telebot.types.InputMediaPhoto(open("Использованные/FirstBranch3.jpg", "rb"))])
        bot.send_message(message.chat.id,
                         'Ты читаешь информацию о студотрядах. На досках большими буквами выведены разные названия. '
                         'На какое название ты обратишь внимание?',
                         reply_markup=get_reply1())
        return

    if message.text == 'ССО "Импульс"' or users.get_student_team(message.chat.id) == "impuls":
        impulsBranch.run(message, users, bot, to_start)
        return
    if message.text == 'СПО "Астра"' or users.get_student_team(message.chat.id) == "astra":
        astraBranch.run(message, users, bot, to_start)
        return
    if message.text == 'Никакое':
        bot.send_message(message.chat.id,
                         'Студотряды тебя не заинтересовали и ты решаешь дальше прогуляться по корпусу (переход на '
                         'другую ветку)')
        to_start()
        return

    bot.send_message(message.chat.id, "Команда не реализована")
