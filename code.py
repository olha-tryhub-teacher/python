   def toggle_show_menu(self):
       if self.is_show_menu:
           self.is_show_menu = False
           self.close_menu()
       else:
           self.is_show_menu = True
           self.show_menu()


   def show_menu(self):
       if self.frame_width <= 200:
           self.frame_width += 5
           self.frame.configure(width=self.frame_width, height=self.winfo_height())
           if self.frame_width >=30:
               self.btn.configure(width=self.frame_width, text="◀️")
       if self.is_show_menu:
           self.after(10, self.show_menu)


   def close_menu(self):
       if self.frame_width >= 0:
           self.frame_width -= 5
           self.frame.configure(width=self.frame_width)
           if self.frame_width >=30:
               self.btn.configure(width=self.frame_width, text="▶️")
       if not self.is_show_menu:
           self.after(10, self.close_menu)


   def change_theme(self, value):
       if value == "Темна":
           set_appearance_mode("dark")
           self.frame.configure(fg_color="dodger blue")
       else:
           set_appearance_mode("light")
           self.frame.configure(fg_color="light blue")


win = MainWindow()
win.mainloop()
