direction = input("Куди рухається Pac-Man?").lower()
move = int(input("Що поруч - введіть число"))
if direction == "ліворуч" or direction == "праворуч" or direction == "вниз" or direction == "вгору":
    if move == 0:
        print(f"Pac-Man може рухатись {direction}.")
    elif move == 1:
        print(f"Pac-Man не може рухатись {direction}.")
    elif move == 2:
        print(f"Pac-Man може з’їсти точку {direction}.")
    elif move == 3:
        print(f"Pac-Man {direction} з’їсть привид.")
    else:
        print("Такого в лабіринті не існує.")
else:
    print("Такого напрямку не існує.")
