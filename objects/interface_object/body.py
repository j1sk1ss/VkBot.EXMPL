class Body:
    def __init__(self, pages, vk):
        self.pages = pages
        self.vk = vk

    def open_page(self, page_name, keyboard):
        for page in self.pages:
            if page.name == page_name:
                page.reveal_page(keyboard)

    def click(self, page_name, button_name, keyboard=None):
        for page in self.pages:
            if page.name == page_name:
                self.open_page(page.click(button_name), keyboard)
