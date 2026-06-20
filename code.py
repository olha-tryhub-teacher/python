# Функція для малювання плосі для правильних літер
def write_ask(word):
    start(-170, 100)
    setheading(0)
    width(4)
    color("black")
    for w in word:
        fd(30)
        penup()
        fd(15)
        pendown()
