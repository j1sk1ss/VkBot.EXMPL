class Body:
    def __init__(self, pages, vk):
        self.pages = pages
        self.vk = vk

    def open_page(self, event=None, page_name="", keyboard=None):
        for page in self.pages:
            if page.name == page_name:
                page.reveal_page(event=event, keyboard=keyboard)

    def click(self, event, button_name):
        for page in self.pages:
            if page.name == event.text:
                page.get_button(button_name).action(event)
