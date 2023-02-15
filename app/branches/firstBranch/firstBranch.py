from app.responseData import ResponseData
from app.database.usersDatabase import UsersData
from app.branches.firstBranch import impulsBranch
from app.branches.firstBranch import astraBranch


def get_student_organisation_keyboard() -> list[str]:
    return ["1. Это трудовой ...",
            "2. Это коллектив, сост...",
            "3. Коллектив, деятельность которого ..."]


def get_reply1() -> list[str]:
    return ['ССО "Импульс"', 'СПО "Астра"', 'Никакое']


def run(user_id: int, request: str, users: UsersData) -> list[ResponseData]:
    users.set_branch(user_id, 1)

    if request == 'Студотряды':
        return [ResponseData(user_id, has_text=True, text="Осмотреть первый этаж, пройтись по коридору"),
                ResponseData(user_id,
                             has_text=True,
                             text='Ты прогуливался по корпусу и заметил ярко оформленные доски со странными названиями.'
                                  ' "Студотряд? Что это?" - подумал ты'
                                  '\n1. Это трудовой коллектив,'
                                  '\n2. Это коллектив, состоящий из студентов,'
                                  '\n3. Коллектив, деятельность которого происходит во внеучебное время',
                             has_keyboard=True,
                             keyboard_items=get_student_organisation_keyboard())
                ]

    if request == '1. Это трудовой ...' \
            or request == '2. Это коллектив, сост...' \
            or request == '3. Коллектив, деятельность которого ...':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Разглядывая фотографии улыбающихся ребят и изучая информацию на досках, ты понял, '
                                  'что студенческие отряды - это трудовые коллективы, сформированные, в основном, '
                                  'из числа обучающихся образовательных организаций высшего образования для совместной'
                                  'работы в свободное от учёбы время (как правило, в период летних каникул)'),
                ResponseData(user_id,
                             has_text=True,
                             text='Ты читаешь информацию о студотрядах. На досках большими буквами выведены разные '
                                  'названия.На какое название ты обратишь внимание?',
                             has_keyboard=True,
                             keyboard_items=get_reply1())]

    if request == 'ССО "Импульс"' or users.get_student_team(user_id) == "impuls":
        return impulsBranch.run(user_id, request, users)
    if request == 'СПО "Астра"' or users.get_student_team(user_id) == "astra":
        return astraBranch.run(user_id, request, users)
    if request == 'Никакое':
        return [ResponseData(user_id,
                             has_text=True,
                             text='Студотряды тебя не заинтересовали и ты решаешь дальше прогуляться по корпусу '),
                ResponseData(user_id, has_text=True,
                             text='Ты прогуливался по корпусу и заметил ярко оформленные доски со странными названиями.'
                                  ' "Студотряд? Что это?" - подумал ты',
                             has_keyboard=True,
                             keyboard_items=get_student_organisation_keyboard()
                             )
                ]

    return [ResponseData(user_id, has_text=True, text="Команда не реализована", do_not_change_keyboard=True)]
