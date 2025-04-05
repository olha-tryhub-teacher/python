print("Художник малює нічне небо 🌌 зі зірками та місяцем 🌙!")
width = int(input("Введіть ширину полотна: "))
height = int(input("Введіть висоту полотна: "))
stars = int(input("Введіть кількість зірок?"))
while (width * height - 1) < stars:
    print("Така кількість зірок не вміститься на картині!")
    stars = int(input("Введіть кількість зірок?"))

count = 1
for y in range(height):
    row = ""
    for x in range(width):
        if y == 0 and x == (width - 1):
            row += "🌙"
            continue
        if count % 3 == 0 and stars > 0:
            row += "⭐️"
            stars -= 1
        else:
            row += "🌌"
        count += 1

    print(row)
