# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
#from vk_api.utils import get_random_id

session = vk_api.VkApi(token='vk1.a.UKZK5aNKj33BB4u5Ws1k1MQ9_rnr7ao_OIcsVwjVE7ViTilzdb6rLEIX6JdCtZE-E_YMFSNsTYg6uBbEx5QgUCYO6sHo8AeOZqEx-YsvAHzNkYjpPoppVPdJA1taVfTwX_VAVJDG8b950-LwgK-U8EhhnnvC-AyZ9Yjheg8SrLz9Ao2EqzPS3kPqppO6cGL8iNVvaKiPt5-GtFc9VeuHGg')
session_api = session.get_api()
longpoll = VkLongPoll(session)

def send_message(id,  text, keyboard=None):
    post = {
        "user_id": id,
        "message": text,
        "random_id": 0
    }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()

    session.method("messages.send", post)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            text = event.text.lower()
            id = event.user_id

            if text == "start":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("Осмотреть 1 этаж, пройтись по корридору", VkKeyboardColor.SECONDARY)

                keyboard.add_line()
                keyboard.add_button("Подняться на 2-й этаж", VkKeyboardColor.SECONDARY)

                keyboard.add_line()
                keyboard.add_button('Подняться на 3-й этаж', VkKeyboardColor.SECONDARY)
                send_message(id, "Ты вошёл в ИРИТ-РТФ", keyboard)

            if text == "Осмотреть 1 этаж, пройтись по корридору":
                keyboard1 = VkKeyboard(one_time=True)
                keyboard1.add_button('1')

                keyboard1.add_line()
                keyboard1.add_button('2')

                keyboard1.add_line()
                keyboard1.add_button('3')
                send_message(id, 'Ты прогуливался по корпусу и заметил ярко оформленные доски со странными названиями. "Студотряд? Что это?" - подумал ты \n'
                                 '1. Это трудовой коллектив\n'
                                 '2. Это коллектив состоящий из студентов\n'
                                 '3. Коллектив, деятельность которого происходит во внеучебное время', keyboard1)
            if text == '1' or text == '2' or text == '3':
                send_message(id, 'Разглядывая фотографии улыбающихся ребят и изучая информацию на досках, ты понял,'
                                 ' что студенческие отряды - это трудовые коллективы, сформированные, в основном, '
                                 'из числа обучающихся образовательных организаций высшего образования для '
                                 'совместной работы в свободное от учёб время (как правило, в период летних каникул)')
                keyboard2 = VkKeyboard(one_time=True)
                keyboard2.add_button('ССО "Импульс"')
                keyboard2.add_line()
                keyboard2.add_button('СПО "Астра"')
                keyboard2.add_line()
                keyboard2.add_button("Никакое")
