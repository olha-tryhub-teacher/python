from customtkinter import *
from PIL import Image


class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Вхід")
        self.resizable(True, False)
        self.name = ""

        # --- ліва частина --
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill="both")

        # ТУТ ЗМІНЮЄМО КАРТІНКУ ДЛЯ ФОНУ
        img_ctk = CTkImage(light_image=Image.open("bg.png"), size=(450, 400))
        self.img_label = CTkLabel(self.left_frame, text="Welcome", image=img_ctk, font=("Helvetica", 50, "bold"))
        self.img_label.pack()
