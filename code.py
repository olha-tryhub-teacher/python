from customtkinter import *

window = CTk()
window.geometry("400x400")
window.title("ДОДАЙТЕ ВАШУ НАЗВУ")

tb = CTkTextbox(window, width=380, height=280)
tb.pack(pady=10, padx=10)

ent = CTkEntry(window, width=380)
ent.pack(pady=10)

b = CTkButton(window, width=380, text="OK")
b.pack()

# window.mainloop()

