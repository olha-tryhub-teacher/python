heating_on = False

def reset():
    global heating_on
    heating_on = False

def control():
    global heating_on
    t = float(input("Введіть вашу температуру: "))

    if t < 18:
        heating_on = True
    elif t > 20:
        heating_on = False

control()
print(heating_on)
control()
print(heating_on)

reset()
print(heating_on)
