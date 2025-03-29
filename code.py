text = input("текст запиту?")
for letter in text:
    if letter in "#$@":
        print(f"Запит містить заборонений символ: {letter}.")
        text = ""
        break

if len(text) > 0:
    print("Запит прийнято.")
