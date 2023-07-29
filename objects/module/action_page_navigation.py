from objects.module.action_module import ActionModule


class ActionPageNavigation(ActionModule):
    def __init__(self, vk, message_text="", user="", address="", body=None, keyboard=None):
        super().__init__(vk, message_text, user)

        self.address = address
        self.body = body
        self.keyboard = keyboard

    def action(self, event):
        self.body.open_page(self.address, self.keyboard)
