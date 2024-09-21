class Widget():
    #властивості класа (в конструкторі)
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
    #методи
    def print_info(self):
        print("Напис: ", self.text)
        print("Розташування: ", self.x, self.y)

class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self, text, x, y, is_clicked):
        super().__init__(text, x, y)
        self.is_clicked = is_clicked
    #нові методи
    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")

#створи екземпляр класа Button
#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click
btn = Button("Реєстрація", 100, 100, False)

answer = input("Хочете зареєструватися? (так / ні):").capitalize()
if answer == "Так":
    btn.click()
else:
    print("А шкода!")
