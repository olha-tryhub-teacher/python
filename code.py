print("🎨 Художник малює квіткове поле!")

# Розміри поля
rows = int(input("Введыть ширину поля:"))
cols =  int(input("Введіть довжину поля"))

# Малюємо поле
for i in range(rows):
    line = ""
    for j in range(cols):
        if (i + j) % 4 == 0:
            line += "🌹"
        elif (i + j) % 4 == 1:
            line += "🌷"
        elif (i + j) % 4 == 2:
            line += "🌼"
        else:
            line += "🌸"
    print(line)
