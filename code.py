def square_fill(a, col):
    color(col)
    begin_fill()
    square(a, col)
    end_fill()


def rectangle_fill(a, b, col):
    color(col)
    begin_fill()
    rectangle(a, b, col)
    end_fill()


def triangle_fill(a, col):
    color(col)
    begin_fill()
    triangle(a, col)
    end_fill()
