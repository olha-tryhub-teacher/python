print("🚴 Велосипедист починає свій шлях від старту до фінішу! 🚴")
dist = int(input("Довжина траси: "))
print("🏁" + dist * "➖" + "🚴" + "🏁")

move = 0
while move < dist:
    m = int(input("Скільки проїхав? "))
    move += m
    if move > dist:
        print("Неможливо! Перепитай художника!")
        move -= m  # Відкатити рух назад
    else:
        print("🏁" + (dist - move) * "➖" + "🚴" + move * "➖" + "🏁")

print("Велосипедист 🚴 успішно доїхав до фінішу! 🏁")
