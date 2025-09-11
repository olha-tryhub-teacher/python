# ваш код
# 1. Ігрове поле
screen.bgcolor("black")
pole = create_t(-150, 150, "turtle", "white")
pole.ht()
pole.begin_fill()
for _ in range(4):
    pole.fd(300)
    pole.lt(90)
pole.end_fill()

# 2. Лейбли - лічильники
# 2.1 Створити лейбли
miss = create_t(-150, 160, "turtle", "red")
miss.count = -1
miss.ht()
catch = create_t(70, 160, "turtle", "green")
catch.count = -1
catch.ht()
