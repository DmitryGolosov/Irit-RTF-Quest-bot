import json
from app.database.userInfo import UserInfo


def from_json(json_str: str):
    str_users = json.loads(json_str)
    d = UsersData()
    for k, v in str_users.items():
        d.users[int(k)] = UserInfo.from_json(v)
    return d


class UsersData:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id: int):
        self.users[user_id] = UserInfo(user_id)

    def remove_user(self, user_id: int):
        if user_id in self.users:
            self.users.pop(user_id)

    def contains(self, user_id: int):
        return user_id in self.users

    def get_student_team(self, user_id: int) -> str:
        if user_id in self.users:
            return self.users[user_id].student_team

    def get_astra_state(self, user_id: int) -> int:
        if user_id in self.users:
            return self.users[user_id].astra_state

    def set_student_team(self, user_id: int, student_team: str):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].student_team = student_team

    def set_astra_state(self, user_id: int, new_state: int):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].astra_state = new_state

    def inc_astra_state(self, user_id: int, delta: int):
        if user_id in self.users:
            self.users[user_id].astra_state += delta

    def set_branch(self, user_id: int, branch: int):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].branch = branch

    def get_branch(self, user_id: int) -> int:
        if user_id in self.users:
            return self.users[user_id].branch

    def to_json(self) -> str:
        str_users = {}
        for k, v in self.users.items():
            str_users[k] = v.to_json()
        return json.dumps(str_users, indent=4)

    def get_friend_name(self, user_id: int) -> str:
        if user_id in self.users:
            return self.users[user_id].friend_name

    def set_friend_name(self, user_id: int, new_name: str):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].friend_name = new_name

    def get_poem_state(self, user_id: int) -> int:
        if user_id in self.users:
            return self.users[user_id].poem_state

    def set_poem_state(self, user_id: int, new_state: int):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].poem_state = new_state

    def get_user_name(self, user_id: int) -> str:
        if user_id in self.users:
            return self.users[user_id].user_name

    def set_user_name(self, user_id: int, new_name: str):
        if user_id not in self.users:
            self.add_user(user_id)
        self.users[user_id].user_name = new_name
