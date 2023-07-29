from vk_api.utils import get_random_id

from objects.module.action_module import ActionModule


class ActionSimpleMessage(ActionModule):
    def action(self, event):
        post = {
            "user_id": self.user,
            "message": self.message_text,
            "random_id": get_random_id()
        }

        if self.user == "":
            post["user_id"] = event.user_id

        self.vk.messages.send(post)
