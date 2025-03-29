max_count = 125
comment = input("Введіть ваш коментар: ")
count = 0
for char in comment:
    if char == " ":
        continue
    count += 1
if count > max_count:
    print( "Коментар не буде опубліковано: досягнуто ліміт у 125 символів.")
else:
    print("Коментар було опубліковано!")
