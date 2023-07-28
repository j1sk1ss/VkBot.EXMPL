from vk_api.utils import get_random_id

from objects.module.action_module import ActionModule


class ActionSimpleMessage(ActionModule):
    def action(self):
        post = {
            "user_id": self.user,
            "message": self.message_text,
            "random_id": get_random_id()
        }

        self.vk.messages.send(post)
