from customtkinter import *

window = CTk()
window.geometry("400x300")
window.title("First App")
window.configure(fg_color="gold")

lbl = CTkLabel(window,
               text="Hello Logika!",  # пишіть це все в один рядок, будь ласка
               width=400,  # пишіть це все в один рядок, будь ласка
               height=150,  # пишіть це все в один рядок, будь ласка
               text_color="navy",  # пишіть це все в один рядок, будь ласка
               font=("Arial", 20, "bold"))  # пишіть це все в один рядок, будь ласка
lbl.pack()

window.mainloop()
