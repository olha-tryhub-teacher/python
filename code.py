    def connect(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(("localhost", 8080))
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

