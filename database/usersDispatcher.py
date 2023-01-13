from database import usersDatabase
from database.usersDatabase import UsersData


def save_users_info(filename: str, users: UsersData):
    with open(filename, "w") as file:
        file.write(users.to_json())


def try_load_users_info_from_json(filename: str) -> UsersData:
    try:
        with open(filename, "r") as file:
            text = file.read()
            return usersDatabase.from_json(text)
    except Exception:
        print("Не удалось загрузить данные пользователей. Создан новый объект")
        return UsersData()
