class Body:
    def __init__(self, pages):
        self.pages = pages

    def open_page(self, page_name, keyboard):
        for page in self.pages:
            if page.name == page_name:
                page.place(keyboard)