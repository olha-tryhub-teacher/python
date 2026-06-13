def draw_field(x_start, y_start, size, col):
    width(4)
    x, y = x_start, y_start
    for i in range(3):
        for j in range(3):
            start(x, y)
            square(size, col)
            x += size
        x = x_start
        y -= size

draw_field(-150, 150, size, "blue")
