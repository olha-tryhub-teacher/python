from customtkinter import *
from socket import *
import threading


from auth import AuthWindow  # ⬅️⬅️⬅️

set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("marsh.json")


auth_win = AuthWindow()  # ⬅️⬅️⬅️
auth_win.mainloop()  # ⬅️⬅️⬅️
name = auth_win.name  # ⬅️⬅️⬅️
ip = auth_win.ip  # ⬅️⬅️⬅️
port = auth_win.port  # ⬅️⬅️⬅️




class MainWindow(CTk):
    def __init__(self,
                 name = ''
                 ):
        super().__init__()
        self.geometry('800x600')
        self.name = name


        self.name_label = CTkLabel(self,
                                   text = f'Привіт {self.name}!')
        self.name_label.pack(pady = 20)


        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.pack(fill = 'both',
                             expand = True)


        self.bottom_frame = CTkFrame(self)
        self.bottom_frame.pack(fill = 'x')


        self.message_entry = CTkTextbox(self.bottom_frame,
                                        height = 40)
        self.message_entry.pack(fill = 'x', expand = True, side = 'left')


        self.send_button = CTkButton(self.bottom_frame,
                                     text = 'Відправити',
                                     width = 50,
                                     height = 40,
                                     command = self.send_message)
        self.send_button.pack()

        self.connect()



    def connect(self):
        try:
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.socket.connect(('localhost', 8080))
            self.socket.send(self.name.encode())
            threading.Thread(target = self.recv_message,
                             daemon = True).start()

        except Exception as ex:
            self.add_message(ex)



    def add_message(self, message):
        label = CTkLabel(self.chat_field,
                         text = message,
                         anchor = 'w',
                         justify = 'left',
                         wraplength = 300)
        label.pack(fill = 'x',
                   anchor = 'w',
                   padx = 5, pady = 2)
        self.chat_field._parent_canvas.yview_moveto(1.0)



    def send_message(self):
        message = self.message_entry.get("1.0", "end-1c")
        if message and self.socket:
            self.socket.send(message.encode())
        self.message_entry.delete("1.0", "end")



    def recv_message(self):
        while True:
            try:
                message = self.socket.recv(1024).decode().strip()
                if message:
                    self.add_message(message)
                else:
                    break

            except Exception as ex:
                self.add_message('')
                self.add_message(ex)
                break





window = MainWindow(name)
window.mainloop()