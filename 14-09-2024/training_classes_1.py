class Button
    def __init_(self, title_text, x_num, y_num):
        self.title = title
        self.x = x
        self.y = y
        self.appearance = True
    def hide( ):
        self.appearance = False
    def show( ):
        self.appearance = True
    def print_status( ):
        print('Дані про віджет:')
        print(self.title, self.x, self.y, self.appearance)

ok_button = Button('ok', 100, 100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()