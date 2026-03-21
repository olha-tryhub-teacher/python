from customtkinter import *

window = CTk()

btn_color = "black"
text_color = "white"

for i in range(8):
    for j in range(8):
        btn = CTkButton(window, width=70, height=70)
        btn.grid(column=i, row=j)

        if (i + j) % 2 == 0:
            btn_color = "black"
            text_color = "white"
        else:
            btn_color = "white"
            text_color = "black"

        btn.configure(fg_color=btn_color, text_color=text_color)


window.mainloop()
