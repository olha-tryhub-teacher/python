    def add_message(self, text):
        label = CTkLabel(self.chat_field, text=text, anchor="w", justify="left", wraplength=300)
        label.pack(fill="x", anchor="w", pady=2, padx=5)
        self.chat_field._parent_canvas.yview_moveto(1.0)  # прокрутка вниз
