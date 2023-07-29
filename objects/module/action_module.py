class ActionModule:
    def __init__(self, vk, message_text="", user=""):
        self.vk = vk
        self.message_text = message_text
        self.user = user

    def action(self, event):
        pass
