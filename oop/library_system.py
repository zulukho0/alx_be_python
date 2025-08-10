class Book:
    def __init__ (self, title: str, auhtor: str):
        self.title = title
        self.author = auhtor


class EBook(Book):
    def __init__ (self, title: str, auhtor: str, file_size: int, page_count: int):
        super().__init__(title, auhtor)
        self.file_size = file_size
        self.page_count = page_count

class PrintBook(Book):
    pass