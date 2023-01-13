from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(unsafe_hash=True)
class UserInfo:
    user_id: int
    branch: int = 0
    student_team: str = "ns"
    astra_state: int = 0
    friend_name: str = "ns"
    poem_state: int = 0
