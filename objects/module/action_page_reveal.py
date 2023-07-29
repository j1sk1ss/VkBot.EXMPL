from objects.module.action_module import ActionModule


class ActionPageReveal(ActionModule):
    def __init__(self, vk, message_text="", user="", page=None):
        super().__init__(vk, message_text, user)

        self.page = page

    def action(self, event):
        if event is None:
            self.page.reveal_page(vk=self.vk, user=self.user)
        else:
            self.page.reveal_page(vk=self.vk, event=event)
