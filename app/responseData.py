from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class ResponseData:
    """Data that the client receives from the application"""
    user_id: int

    has_text: bool = False
    has_keyboard: bool = False
    has_image: bool = False
    do_not_change_keyboard: bool = False

    text: str = ""
    keyboard_items: list[str] = None
    images_path: list[str] = None

