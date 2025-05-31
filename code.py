new_coordinates = []

for i in range(0, len(coordinates), 2):
    x = coordinates[i]
    y = coordinates[i + 1]
    if 0 <= x <= 50 and 0 <= y <= 50:
        new_coordinates.append(x)
        new_coordinates.append(y)

for i in range(0, len(new_coordinates), 2):
    print("x:", new_coordinates[i], "; y:", new_coordinates[i + 1])
