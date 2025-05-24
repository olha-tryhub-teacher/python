# юніт 2, завдання 3

# Виводить список курсорів у стовпчик.
def display_cursors(cursors):
    for c in cursors:
        print(c)


while True:
    display_cursors(cursors)
    ans = input("Який курсор видалити?")
    if ans != "0":
        if ans in cursors:
            cursors.remove(ans)
            print(f"Курсор '{ans}' видалено.")
        else:
            print("Такого курсора немає у списку. Спробуйте ще раз.")
    else:
        break
print(cursors)

# юніт 3

pixel_size = 10
x,y = -100,100
for line in pic_map:
    for num in line:
        penup()
        goto(x,y)
        pendown()
        c = colors_map[int(num)]
        square_fill(pixel_size,c)
        x+=pixel_size
    x = -100
    y -= pixel_size

# 3.3

pixel_sizes = 10
coordinates = [-200,0,140,160,-20,50]
pixel_size = 10

def drawPix(x,y, pic_map, colors_map):
    x_start = x
    for line in pic_map:
        for num in line:
            start(x,y)
            if num != "-":
                squareFill(pixel_size,colors_map[int(num)])
            x += pixel_size 
        x = x_start
        y -= pixel_size 
start(-300,-300)
squareFill(800,"#bbeef9")
drawPix(coordinates[0],coordinates[1],pic_map1,colors_map1)
drawPix(coordinates[2],coordinates[3],pic_map2,colors_map2)
drawPix(coordinates[4],coordinates[5],pic_map3,colors_map3)
