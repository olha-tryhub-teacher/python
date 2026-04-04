purchase_limit = 500
count = 0
while count <= purchase_limit:
    price = float(input("Введіть суму покупок?"))
    count += price
    print(f"Всього покупок: {count}")
if count - purchase_limit >= 200:
    print("Ліміт покупки значно перевищено!")
