from customtkinter import *


class MainWindow(CTk):
   def __init__(self):
       super().__init__()
       self.geometry("400x400")


       self.frame= CTkFrame(self, fg_color="light blue", width=200, height=self.winfo_height())
       self.frame.pack_propagate(False)
       self.frame.configure(width=0)
       self.frame.place(x=0, y=0)
       self.is_show_menu = False
       self.frame_width = 0


       self.label = CTkLabel(self.frame, text="Ваше Ім`я")
       self.label.pack(pady=30)
       self.entry = CTkEntry(self.frame)
       self.entry.pack()
       self.label_theme = CTkOptionMenu(self.frame, values=["Світла", "Темна"], command=self.change_theme)
       self.label_theme.pack(side="bottom", pady=120)
       self.theme = None
       self.btn = CTkButton(self, text="▶️", command=self.toggle_show_menu, width=30)
       self.btn.place(x=0, y=0)


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
