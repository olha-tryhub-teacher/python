
class Book():
    def __init__(self, title, total_pages):
        self.title = title
        self.pages = total_pages
        self.__current_page = 1

    def set_current_page(self, new_current_page):
        if new_current_page <= self.pages:
            self.__current_page = new_current_page
        else:
            print(f"Номер сторінки занадто великий! Всього у книжці {self.pages} сторінок!")

    def get_current_page(self):
        print(f"Зараз ми на {self.__current_page} сторінці")


b1 = Book("title", 555)
# b1.current_page = 111111
b1.__current_page = 111111

b1.get_current_page()
b1.set_current_page(666)
b1.set_current_page(23)
b1.get_current_page()
