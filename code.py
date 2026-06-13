coordinates = [12, 45, 34, 23, 50, 60, -10, 15, 25, 25]
new_coordinates = list()
#0 <= x <= 50 і 0 <= y <= 50
for i in range(0,len(coordinates),2):
  if 0 <= coordinates[i] <= 50 and 0 <= coordinates[i+1] <= 50:
    new_coordinates.append(coordinates[i])
    new_coordinates.append(coordinates[i+1])
    

for i in range(0,len(new_coordinates),2):
  print(f"x: {new_coordinates[i]} ; y: {new_coordinates[i+1]}")
