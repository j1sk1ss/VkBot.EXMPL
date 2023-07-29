from vk_api.utils import get_random_id

from objects.module.action_module import ActionModule


class ActionSimpleMessage(ActionModule):
    def __init__(self, vk, message_text="", user="", buttons=None, keyboard=None):
        super().__init__(vk, message_text, user)

        self.buttons = buttons
        self.keyboard = keyboard

    def action(self, event):
        for button in self.buttons:
            button.place(self.keyboard)

        post = {
            "user_id": self.user,
            "message": self.message_text,
            "random_id": get_random_id(),
            "keyboard": self.keyboard
        }

        if self.user == "":
            post["user_id"] = event.user_id

        self.vk.messages.send(post)
