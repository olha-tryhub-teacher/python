def write_right(letter, word):
    start(-170, 105)
    penup()
    color("black")
    setheading(0)
    count = 0
    for w in word:
        if w == letter:
            pendown()
            write(letter, font=("Arial", 32))
            penup()
            count += 1
        fd(45)
    return count
