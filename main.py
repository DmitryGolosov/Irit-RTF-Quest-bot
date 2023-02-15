import os
import threading

from clients import telegramBot
from clients import VkBot
from app.database import usersDispatcher


if __name__ == '__main__':
    global activate
    user_data_filename = os.path.dirname(os.path.abspath(__file__)) + '/app/database/usersData.json'
    users = usersDispatcher.try_load_users_info_from_json(user_data_filename)

    tg = threading.Thread(target=telegramBot.run, args=[users])
    tg.daemon = True
    vk = threading.Thread(target=VkBot.run, args=[users])
    vk.daemon = True

    tg.start()
    vk.start()

    tg.join()
    vk.join()

    usersDispatcher.save_users_info(user_data_filename, users)
    print("Данные сохранены")
