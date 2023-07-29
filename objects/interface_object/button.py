class Button:
    def __init__(self, name, keyboard=None, action_module=None):
        self.name = name
        self.keyboard = keyboard
        self.action_module = action_module

    def place(self, keyboard):
        keyboard.add_button(self.name)

    def action(self, event):
        self.action_module.action(event)
