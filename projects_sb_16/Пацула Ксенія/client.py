from customtkinter import *
import threading  # ⬅️
from socket import *  # ⬅️

set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("themes/midnight.json")

from auth import AuthWindow

auth_win = AuthWindow()
auth_win.mainloop()
name = auth_win.name
ip = auth_win.ip
port = auth_win.port

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
        self.send_button = CTkButton(self.bottom_row,
                                     text=">",
                                     width=50,
                                     height=40,
                                     command=self.send_message)  # ⬅️⬅️⬅️
        self.send_button.pack(side="left")

        self.connect()

    def connect(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((ip, port))
            self.sock.send(self.username.encode())
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:  # ⬅️
            self.add_message(f"Не вдалося підключитися до сервера: {e}")

    def add_message(self, text):
        label = CTkLabel(self.chat_field, text=text,
                         anchor="w", justify="left",
                         wraplength=300)
        label.pack(fill="x", anchor="w", pady=2, padx=5)
        self.chat_field._parent_canvas.yview_moveto(1.0)  # прокрутка вниз

    def send_message(self):
        message = self.message_entry.get()
        if message and self.sock:
            self.sock.send(message.encode())
        self.message_entry.delete(0, END)

    def recv_message(self):
        while True:
            try:
                message = self.sock.recv(1024).decode().strip()
                if message:
                    self.add_message(message)
                else:
                    break
            except Exception as e:
                self.add_message("Від'єднано від сервера")
                self.add_message(e)
                break


main_win = MainWindow()
main_win.mainloop()