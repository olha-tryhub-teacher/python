for i in range(3):
    count = int(input("кількість товарів для замовлення?"))
    if count > 10:
        print("Перевищено ліміт! Повторіть спробу.")
        count = -1
        continue
    else:
        print(f"Замовлено {count} товарів.")
        break

if count == -1:
    print("Замовлення не прийнято.")
