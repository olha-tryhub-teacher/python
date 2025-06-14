from turtle import *
from art import *
#підключи модуль turtle
#встанови швидкість(speed) черепашки - 0 
#перший малюнок - список кольорів та закодований малюнок
colors_map1 = ["#a7adad", "#fafafa", "#4064f9 ", "#080808","#f09510 "]
pic_map1 = [ "------000------",
            "------000------",
            "-----11111-----",
            "---111111111---",
            "--11111111111--",
            "-1111221221111-",
            "-1111231231111-",
            "111111144111111",
            "111111444441111",
            "111311144444411",
            "111333311133111",
            "-1113333331111-",
            "-1111333331111-",
            "--11113331111--",
            "---111111111---",
            "-----11111-----"]

            
tracer(9)
pixel_sizes = 10
coordinates = [-200,0,140,160,-20,50]
pixel_size = 10

def drawPix(x,y, pic_map, colors_map):
    x_start = x
    for line in pic_map:
        for num in line:
            start(x,y)
            if num != "-":
                square_fill(pixel_size,colors_map[int(num)])
            x += pixel_size 
        x = x_start
        y -= pixel_size 
start(-300,-300)
square_fill(800,"#bbeef9")
drawPix(-200,0,pic_map1,colors_map1)
