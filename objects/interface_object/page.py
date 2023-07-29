from vk_api.utils import get_random_id

from enums.message_type import MessageType


class Page:
    def __init__(self, name, message, buttons, message_type, attachment):
        self.name = name
        self.message = message
        self.buttons = buttons
        self.message_type = message_type
        self.attachment = attachment

    def reveal_page(self, vk, event, user="", keyboard=None):
        for button in self.buttons:
            button.reveal_page(keyboard)

        post = {
            "user_id": user,
            "message": self.message,
            "random_id": get_random_id()
        }

        if user == "":
            post["user_id"] = event.user_id

        if self.message_type == MessageType.wall_post:
            post["attachment"] = self.attachment

        if self.message_type == MessageType.keyboard:
            post["keyboard"] = keyboard.get_keyboard()

        vk.messages.send(post)

    def get_button(self, name):
        for button in self.buttons:
            if button.click(name=name):
                return button
