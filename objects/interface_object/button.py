from vk_api.utils import get_random_id

from enums.message_type import MessageType


def send_message(vk, event, message_type, message="", attachment="", keyboard=None):
    post = {
        "user_id": event.user_id,
        "message": message,
        "random_id": get_random_id()
    }

    if message_type == message_type.wall_post:
        post["attachment"] = attachment

    if message_type == message_type.keyboard:
        post["keyboard"] = keyboard.get_keyboard()

    vk.messages.send(post)


class Button:
    def __int__(self, vk, message, message_type=MessageType.text, attachment="", keyboard=None):
        self.message = message
        self.vk = vk
        self.message_type = message_type
        self.attachment = attachment
        self.keyboard = keyboard

    def place(self, keyboard):
        keyboard.add_button(self.message)

    def click(self, event):
        send_message(self.vk, event, self.message_type, self.message, self.attachment, self.keyboard)
