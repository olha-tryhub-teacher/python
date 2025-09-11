# 4. Яблука
# 4.1 Список яблук
apples = []
colors = ["red", "gold", "blue"]


# 4.2 Функція появи нового яблука
def spawn_a():
    a = create_t(randint(-130, 130), 150, "circle", choice(colors))
    apples.append(a)


# 4.3 Функця руху яблука
def move(a):
    a.fd(5)


# 4.4 Функція перевірки яблука, що впало
def check_miss(a):
    if a.ycor() <= - 150:
        a.ht()
        apples.remove(a)
        update_count(miss, "Miss")


# 4.5 Функція спійманого яблука
def check_catch(a):
    x, y = plt.xcor(), plt.ycor()
    if a.distance(x, y) <= 10:
        a.ht()
        apples.remove(a)
        update_count(catch, "Catch")


# 5. Функція перевірка виграшу/програшу
def check_end_game():
    if miss.count >= 3:
        miss.goto(0, 0)
        miss.write("You lose", font=("Arial", 14))
        return True
    if catch.count >= 10:
        catch.goto(0, 0)
        catch.write("You win", font=("Arial", 14))
        return True
    return False


# 6. Функція гри
def game():
    if randint(1, 30) == 3:
        spawn_a()
    for a in apples:
        move(a)
        check_miss(a)
        check_catch(a)
    end = check_end_game()
    if not end:
        screen.ontimer(game, 50)


# Запускаємо все
update_count(miss, "Miss")
update_count(catch, "Catch")
spawn_a()
game()
