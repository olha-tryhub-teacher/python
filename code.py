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
