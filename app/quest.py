from app.responseData import ResponseData
from app.branches.firstBranch import firstBranch
from app.branches.secondBranch import secondBranch
from app.branches.thirdBranch import thirdBranch
from app.database.usersDatabase import UsersData



def get_main_keyboard_items() -> list[str]:
    return ["Студотряды", "Традиции ИРИТ-РТФ", "Известные выпускники ИРИТ-РТФ"]


def get_start_keyboard_items() -> list[str]:
    return ["Поехали"]


def ask_user_name(user_id: int, users: UsersData) -> list[ResponseData]:
    users.set_user_name(user_id, "$asked$")
    return [ResponseData(user_id, has_text=True,
                         text="Кажется мы ещё не знакомы. Как тебя зовут?")]


def save_user_name(user_id: int, request: str, users: UsersData) -> list[ResponseData]:
    users.set_user_name(user_id, request)
    return [ResponseData(user_id,
                         has_text=True,
                         text='С чего ты хотел(-а) бы начать?',
                         has_keyboard=True,
                         keyboard_items=get_main_keyboard_items())]


def start(user_id: int, users: UsersData) -> ResponseData:
    users.add_user(user_id)
    return ResponseData(user_id,
                        has_text=True,
                        text="Привет!\n"
                             "Это создатели данного квеста и мы предлагаем тебе ознакомиться с его "
                             "содержанием. Если ты хочешь узнать традиции ИРИТ-РТФ, историю студотрядов или "
                             "известных людей, которые закончили ИРИТ-РТФ, то нажимай кнопку ПОЕХАЛИ и начнем "
                             "наше приключение!\nДля остановки бота введите /stop",
                        has_keyboard=True,
                        keyboard_items=get_start_keyboard_items())


def stop(user_id: int, users: UsersData) -> ResponseData:
    users.remove_user(user_id)
    return ResponseData(user_id, has_text=True,
                        text="Бот успешно отключен. До свидания.\nДля начала работы введите /start")


def main_story(user_id: int, request: str, users: UsersData) -> list[ResponseData]:
    if not users.contains(user_id):
        return [ResponseData(user_id, has_text=True,
                             text="Неправильное начало диалога. Воспитанные люди сначал пишут /start")]

    if request == 'Поехали':
        return ask_user_name(user_id, users)

    if users.get_user_name(user_id) == "$asked$":
        return save_user_name(user_id, request, users)

    if request == 'Студотряды' or users.get_branch(user_id) == 1:
        return firstBranch.run(user_id, request, users)

    if request == 'Традиции ИРИТ-РТФ' or users.get_branch(user_id) == 2:
        return secondBranch.run(user_id, request, users)

    if request == 'Известные выпускники ИРИТ-РТФ' or users.get_branch(user_id) == 3:
        return thirdBranch.run(user_id, request, users)

    return [ResponseData(user_id, has_text=True, text="Команда не реализована", do_not_change_keyboard=True)]
