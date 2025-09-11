# 2.2 Функція що оновлює напис
def update_count(label, txt):
    label.count += 1
    label.clear()
    label.write(f"{txt} : {label.count}", font=("Arial", 16))


# 3.Платформа-гравець
# 3.1 Створити гравця
plt = create_t(0, -130, "square", "violet")


# 3.2 Функції руху праворчу-ліворуч
def move_l():
    plt.setheading(180)
    plt.fd(10)

def move_r():
    plt.setheading(0)
    plt.fd(10)

# 3.3 Підписка на події клавіші
screen.onkey(move_l, "Left")
screen.onkey(move_r, "Right")
screen.listen()
