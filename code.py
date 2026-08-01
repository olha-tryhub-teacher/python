redPainter.setheading(90)
greenPainter.setheading(210)
bluePainter.setheading(330)

redPainter.speed(0)
bluePainter.speed(0)
bluePainter.speed(0)
# ваш код
for i in range(150):
    redPainter.fd(1)
    redPainter.lt(2)
    greenPainter.fd(1)
    greenPainter.lt(2)
    bluePainter.fd(1)
    bluePainter.lt(2)
