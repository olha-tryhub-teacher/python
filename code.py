h = input("Висота клумби:")
w = input("Ширина клумби:")
if h.isdigit() and w.isdigit():
    h, w = int(h), int(w)
    if h > 0 and w > 0:
        for i in range(h):
            if i == 0 or i == (h - 1):
                print(w * "🧱")
            else:
                print("🧱" + (w - 2) * "🌹" + "🧱")
        print("Клумба готова! Архітектор пишається вашою роботою!")
    else:
        print("Клумба не може бути із розмірами 0!")
else:
    print("Розміри клумби мають бути числами!")
