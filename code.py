# 1
# ваш код:
class Pupil():
    def __init__(self, name, age=12):
        self.name = name
        self.age = age

    def say(self):
        print(f"Hello! My name is {self.name}. " # можна в один рядок
              f"I am {self.age} years old!")


p1 = Pupil("Olia", 25)
p1.say()


# 2
# ваш код

class Book():
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        self.current_page = 1

    def set_current_page(self, new_current_page):
        if new_current_page <= self.pages:
            self.current_page = new_current_page
        else:
            print(f"Номер сторінки занадто великий! Всього у книжці {self.pages} сторінок!")

    def get_current_page(self):
        print(f"Зараз ми на {self.current_page} сторінці")


b1 = Book("title", 555)


b1.get_current_page()
b1.set_current_page(666)
b1.set_current_page(23)
b1.get_current_page()
