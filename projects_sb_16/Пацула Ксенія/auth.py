from customtkinter import *
from PIL import Image



class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Вхід")
        self.resizable(True, False)
        self.name = ""

        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill="both")

        img_ctk = CTkImage(light_image=Image.open("img.png"), size=(450, 400))
        self.img_label = CTkLabel(self.left_frame, text="Welcome", image=img_ctk, font=("Helvetica", 50, "bold"))
        self.img_label.pack()

        self.right_frame = CTkFrame(self)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand="True")

        CTkLabel(self.right_frame, text="LogiTalk").pack(pady=60)

        self.name_entry = CTkEntry(self.right_frame, placeholder_text="ім'я")
        self.name_entry.pack(fill="x", padx=10, pady=10)

        self.ip_entry = CTkEntry(self.right_frame, placeholder_text="IP адресс")
        self.ip_entry.pack(fill="x", padx=10, pady=10)

        self.port_entry = CTkEntry(self.right_frame, placeholder_text="Порт сервер")
        self.port_entry.pack(fill="x", padx=10, pady=10)

        self.connect_button = CTkButton(self.right_frame, text="УВІЙТИ", command=self.open_messenger)
        self.connect_button.pack(fill="x", padx=10, pady=5)

    def open_messenger(self):
        self.name = self.name_entry.get()
        self.ip = self.ip_entry.get()
        self.port = int(self.port_entry.get())
        self.destroy()

# AuthWindow().mainloop()