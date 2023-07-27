class Page:
    def __init__(self, name, buttons):
        self.name = name
        self.buttons = buttons

    def place(self, keyboard):
        for button in self.buttons:
            button.place(keyboard)

    def click(self, name, event):
        for button in self.buttons:
            if button.message == name:
                button.click(event)
