from customtkinter import *
from socket import *
import threading
from aute import AuthWindow
from PIL import Image

set_appearance_mode("dark")
set_default_color_theme("violet.json")

img=Image.open('img_2.png')
imag = CTkImage(dark_image=img, size=(30, 30))

auth_win = AuthWindow()
auth_win.mainloop()
name = auth_win.name
ip = auth_win.ip
port = auth_win.port


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("390x400")
        self.configure(cursor="heart")
        self.title("Мяукалка")

        self.uname = name
        self.name_lbl = CTkLabel(self, text="Мяу-Мяу, " + self.uname, text_color="pink")
        self.name_lbl.pack(pady=20)

        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.pack(fill="both", expand=True)

        self.Buttom_row = CTkFrame(self)
        self.Buttom_row.pack(fill="x")

        self.message = CTkEntry(self.Buttom_row, placeholder_text="Мяукай: ", height=40, placeholder_text_color="pink")
        self.message.pack(fill="x", expand=True, side='left')

        self.send = CTkButton(self.Buttom_row, text="мур", text_color="violet", image=imag, compound="left", height=40, width=50, command=self.send_message, fg_color="black")
        self.send.pack()
        self.connect()

    def connect(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(("localhost", 8080))
            self.sock.send(self.uname.encode())
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"Не вдалося підключитися до сервера: {e}")

    def add_message(self, text):
        label = CTkLabel(self.chat_field, text=text,
                         anchor="w", justify="left",
                         wraplength=300)
        label.pack(fill="x", anchor="w", pady=2, padx=5)
        self.chat_field._parent_canvas.yview_moveto(1.0)

    def send_message(self):
        message = self.message.get()
        if message and self.sock:
            self.sock.send(message.encode())
        self.message.delete(0, END)

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


window = MainWindow()
window.mainloop()