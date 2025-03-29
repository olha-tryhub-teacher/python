from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance


win = CTk()
win.geometry('600x600')
set_default_color_theme('green')


image = Image.open('img.png')
image_ctk = CTkImage(light_image=image, size=(350, 250))


label_img = CTkLabel(win, text='', image=image_ctk)
label_img.pack(pady=100)


set_frame = CTkFrame(win)
set_frame.pack(side='bottom', pady=20)


angle_img = 0
def rotate_image():
   global angle_img, image
   if angle_img <= 360:
       angle_img += 90
       image_ctk.configure(light_image=image.rotate(angle_img))
   else:
       angle_img = 0
   label_img.configure(image=image_ctk)


def block_white():
   global image
   image = image.convert('L')
   image_ctk.configure(light_image=image)
   label_img.configure(image=image_ctk)


def blur_img():
   global image
   image = image.filter(ImageFilter.BLUR)
   image_ctk.configure(light_image=image)
   label_img.configure(image=image_ctk)


def enhance_contrast(value):
   global image
   enhancer = ImageEnhance.Contrast(image)
   image = enhancer.enhance(value/50)
   image_ctk.configure(light_image=image)
   label_img.configure(image=image_ctk)


btn_rotate = CTkButton(set_frame, text='Повернти на 90', command=rotate_image)
btn_rotate.grid(row=0, column=0, padx=10)


btn_l = CTkButton(set_frame, text='ЧБ', command=block_white)
btn_l.grid(row=0, column=1, padx=10)


btn_blur = CTkButton(set_frame, text='Розмиття', command=blur_img)
btn_blur.grid(row=0, column=2, padx=10)


label = CTkLabel(set_frame, text='Контраст')
label.grid(row=1, column=0)


slide_enchance = CTkSlider(set_frame, from_=0, to=100, command=enhance_contrast)
slide_enchance.grid(row=1, column=1, pady=5)


win.mainloop()
