print("Архітектор хоче створити клумбу з трояндами 🌹!")
height = input("Введіть висоту клумби: ")
width = input("Введіть ширину клумби: ")
if height.isdigit() and width.isdigit():
    height = int(height)
    width = int(width)
    print(width * "🧱")
    for i in range(height - 2):
        print("🧱" + (width - 2) * "🌹" + "🧱")
    print(width * "🧱")

    print("Клумба готова! Архітектор пишається вашою роботою!")
else:
    print("Розміри клумби мають бути числами!")
