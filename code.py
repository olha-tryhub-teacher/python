def drawGalows(count):
    x, y = getCor(coordinats[count - 1])
    start(x, y)
    color("grey")
    width(10)
    # 1 ОСНОВА
    if count == 1:
        setheading(0)
        fd(40)
        # 2 СТОВП
    elif count == 2:
        setheading(90)
        fd(210)
        # 3  ПЕРЕКЛАДИНА 1
    elif count == 3:
        setheading(180)
        fd(95)
        # 4 ПЕРЕКЛАДИНА 2
    elif count == 4:
        setheading(270 + 45)
        fd(65)
        # 5 МОТУЗКА 1
    elif count == 5:
        setheading(270)
        fd(40)
        # 6 МОТУЗКА 2
    elif count == 6:
        width(5)
        setheading(0)
        for i in range(4):
            setheading(180)
            pendown()
            fd(20)
            penup()
            setheading(270)
            fd(5)
            setheading(0)
            pendown()
            fd(20)
        bk(10)
        setheading(270)
        fd(15)

        # 7 ГОЛОВА
    elif count == 7:
        width(3)
        circle(25)
        # ОЧІ ТА СУМНА УСМІШКА - НЕОБОВ’ЯЗКОВАЧАСТИНА
        start(x + 5, y + 30)
        setheading(270 + 45)
        fd(15)
        start(x + 10, y + 30)
        setheading(270 - 45)
        fd(15)
        start(x + 25, y + 30)
        setheading(270 + 45)
        fd(15)
        start(x + 31, y + 30)
        setheading(270 - 45)
        fd(15)
        start(x + 10, y)
        setheading(45)
        circle(-17, 100)

        # 8 РУКА 1
    elif count == 8:
        setheading(290)
        width(4)
        pendown()
        fd(45)
        # 9 РКА 2
    elif count == 9:
        width(4)
        setheading(250)
        pendown()
        fd(45)
        # 10 ТІЛО
    elif count == 10:
        setheading(0)
        width(4)
        pendown()
        setheading(270)
        fd(60)
        # 11 НОГА 1
    elif count == 11:
        width(4)
        setheading(270 - 45)
        fd(45)

        # 12 НОГА 2
    elif count == 12:
        width(4)
        setheading(270 + 45)
        fd(45)
