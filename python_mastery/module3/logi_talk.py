from customtkinter import *
import threading
from socket import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("light")  # світла тема

        self.geometry("500x400")
        self.title("Фіолетовий Чат")

        self.label = None

        # menu frame
        self.menu_frame = CTkFrame(self, width=30, height=300, corner_radius=0, fg_color="#e8e8f0")
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)

        self.is_show_menu = False
        
        self.speed_animate_menu = -5

        self.btn = CTkButton(self, text="▶️", command=self.toggle_show_menu,
                             width=30, fg_color="#bbaadd", hover_color="#aa99cc", text_color="white")
        self.btn.place(x=0, y=0)

        # chat field
        self.chat_field = CTkScrollableFrame(self, fg_color="#f5f5fb", corner_radius=10)
        self.chat_field.place(x=0, y=0)

        # message entry
        self.message_entry = CTkEntry(self, placeholder_text="Введіть повідомлення:",
                                      height=40, corner_radius=10, border_color="#cc99ff", border_width=2)
        self.message_entry.place(x=0, y=0)

        self.send_button = CTkButton(self, text="➤", width=50, height=40, command=self.send_message,
                                     fg_color="#cc99ff", hover_color="#b380f0", corner_radius=10,
                                     text_color="white")
        self.send_button.place(x=0, y=0)

        self.username = "Оля"

        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(("localhost", 8080))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
            self.sock.send(hello.encode("utf-8"))
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"Не вдалося підключитися до сервера: {e}")

        self.adaptive_ui()


    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text="▶️")
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text="◀️")
            self.show_menu()
            # setting menu widgets
            self.label = CTkLabel(self.menu_frame, text="Імʼя")
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()
            # кнопка для зберігання імені
            self.save_name_button = CTkButton(self.menu_frame, text="Зберегти",
                                              command=self.save_name,
                                              fg_color="#cc99ff", hover_color="#b380f0",
                                              corner_radius=10,
                                              text_color="white")
            self.save_name_button.pack(pady=10)

    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
        if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width() >= 40 and not self.is_show_menu:
            self.after(10, self.show_menu)
            if self.label and self.entry:
                self.label.destroy()
                self.entry.destroy()
                self.save_name_button.destroy()

    def adaptive_ui(self):
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(width=self.winfo_width() - self.menu_frame.winfo_width() - 20,
                                  height=self.winfo_height() - 40)
        self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - self.send_button.winfo_width())

        self.after(50, self.adaptive_ui)

    def add_message(self, text):
        bubble = CTkFrame(self.chat_field, fg_color="#e6ddff", corner_radius=8)
        label = CTkLabel(bubble, text=text, anchor="w", justify="left", wraplength=360,
                         font=("Arial", 12), text_color="#2d1152")
        label.pack(padx=6, pady=4)
        bubble.pack(fill="x", anchor="w", pady=4, padx=10)
        self.chat_field._parent_canvas.yview_moveto(1.0)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.add_message(f"{self.username}: {message}")
            data = f"TEXT@{self.username}@{message}\n"
            try:
                self.sock.sendall(data.encode())
            except:
                pass
        self.message_entry.delete(0, END)

    def recv_message(self):
        buffer = ""
        while True:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buffer += chunk.decode()

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.handle_line(line.strip())
            except:
                break
        self.sock.close()

    def handle_line(self, line):
        if not line:
            return
        parts = line.split("@", 3)
        msg_type = parts[0]

        if msg_type == "TEXT":
            if len(parts) >= 3:
                author = parts[1]
                message = parts[2]
                self.add_message(f"{author}: {message}")
        else:
            self.add_message(line)

    # методля длязберігання імені
    def save_name(self):
        new_name = self.entry.get()
        if new_name:
            self.username = new_name
            self.add_message(f"[SYSTEM] Імʼя змінено на: {new_name}")


win = MainWindow()
win.mainloop()
