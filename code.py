# створити черепашок
t1 = create_turtle(-150, 70, "turtle", "purple")
t2 = create_turtle(-150, -70, "turtle", "orange")

track()

# створити ігровий цикл, де черепашки будуть змагатись
while t1.xcor() < 300 and t2.xcor() < 300:
    t1.forward(randint(1, 7)) # 7
    t2.forward(randint(1, 7)) # 1


if t1.xcor() > t2.xcor(): #305, 301
    win(t1)
else:
    win(t2)
