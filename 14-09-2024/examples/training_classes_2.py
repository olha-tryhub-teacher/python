class Title():
    #конструктор
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    #методи
    def hide(self):
        self.appearance = False
        print("✨ Напис", self.title, "приховано")

    def show(self):
        self.appearance = True
        print("✨ Напис", self.title, "показано")

    def print_status(self):
        print('✅ Дані про віджет:')
        print(self.title, self.x, self.y, self.appearance)
#створи два написи
#приховай другий напис

title1 = Title('Hello!', 100, 100)
title2 = Title('Bye!', 100, 200)
title1.print_status()
title2.print_status()
title2.hide()
title2.print_status()