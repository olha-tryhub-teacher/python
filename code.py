print("🚴 Велосипедист починає свій шлях від старту до фінішу! 🚴")
finish = ""
dist = int(input("Довжина траси:"))
velo = "🏁" + dist * "➖" + "🚴" + "🏁"
velo += "\n"
back = 0
while dist > 0:
    move = int(input("Скільки проїхав?"))
    if dist - move >= 0:
        back += move
        dist = dist - move
        row = dist * "➖" + "🚴" + back * "➖"
        velo += "🏁" + row + "🏁" + "\n"
    else:
        print("Неможливо! Перепитай художника!")
print(velo)

print("Велосипедист 🚴 успішно доїхав до фінішу! 🏁")
