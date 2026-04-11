from customtkinter import *

name = "Оля"


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        # main
        self.username = name
        self.name_lbl = CTkLabel(self, text="Привіт, " + self.username)
        self.name_lbl.pack()
        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.pack(fill="both", expand=True)

        self.bottom_row = CTkFrame(self)
        self.bottom_row.pack(fill="x")

        self.message_entry = CTkEntry(self.bottom_row,
                                      placeholder_text="Введіть повідомлення:",
                                      height=40)
        self.message_entry.pack(fill="x", side="left", expand=True)
        self.send_button = CTkButton(self.bottom_row, text=">", width=50, height=40)
        self.send_button.pack(side="left")


main_win = MainWindow()
main_win.mainloop()
