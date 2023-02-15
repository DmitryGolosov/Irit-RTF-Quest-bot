import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from time import sleep
from clients import config
from app import quest
from app.responseData import ResponseData
from app.database.usersDatabase import UsersData

vk = vk_api.VkApi(token=config.vk_token)
longpoll = VkLongPoll(vk)
users = UsersData()


def create_keyboard(items: list[str]):
    is_first_line = True
    keyboard = VkKeyboard(one_time=False)
    for item in items:
        if not is_first_line:
            keyboard.add_line()
        keyboard.add_button(item, VkKeyboardColor.SECONDARY)
        is_first_line = False
    return keyboard


def send_message(user_id, msg_text, msg_keyboard=None, remove_keyboard=False):
    post = {
        "user_id": user_id,
        "message": msg_text,
        "random_id": 0
    }
    if remove_keyboard:
        post["keyboard"] = VkKeyboard().get_empty_keyboard()
    if msg_keyboard is not None:
        post["keyboard"] = msg_keyboard.get_keyboard()
    vk.method("messages.send", post)


def send_photos_in_message(user_id: int, photos_info: str):
    post = {
        "user_id": user_id,
        "attachment": photos_info,
        "random_id": 0
    }
    vk.method("messages.send", post)


def upload_photos_get_info(paths: list[str]) -> str:
    upload = vk_api.VkUpload(vk)
    photos_info = []
    for path in paths:
        owner_id, photo_id, access_key = upload_photo_get_info(upload, path)
        photos_info.append(f'photo{owner_id}_{photo_id}_{access_key}')

    return ','.join(photos_info)


def upload_photo_get_info(upload, path: str):
    photo = upload.photo_messages(path)[0]

    owner_id = photo['owner_id']
    photo_id = photo['id']
    access_key = photo['access_key']

    return owner_id, photo_id, access_key


def send_messages(data: list[ResponseData]):
    for message in data:
        if message.has_image:
            images_info = upload_photos_get_info(message.images_path)
            send_photos_in_message(message.user_id, images_info)

        keyboard = None
        if message.has_keyboard:
            keyboard = create_keyboard(message.keyboard_items)

        if message.has_text:
            send_message(message.user_id, message.text, keyboard, not message.do_not_change_keyboard)
            sleep(0.08)


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                text = event.text
                user_id = event.user_id

                if text == config.stop_passwd:
                    raise Exception("Bot stopped by stop passwd")

                if text == "start" or text == "Привет":
                    send_messages([quest.start(user_id, users)])
                    continue

                if text == "/stop" or text == "Стоп":
                    send_messages([quest.stop(user_id, users)])
                    continue

                send_messages(quest.main_story(user_id, text, users))


def run(users_db: UsersData):
    global users
    users = users_db
    try:
        print("Запуск вк бота")
        main()
    except Exception as e:
        print(f"Хьюстон, у вк большие проблемы\n{e}")
