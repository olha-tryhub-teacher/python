from turtle import *
from art import *
from guess_word import *
from random import choice

## Список кольорів пелюсток
colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f", "#e74c3c", "#5dade2"]

# координати для відображення неправильних літер
x_wrong, y_wrong = -170, 50

# радіус пелюстки та листочків
r = 95
# стартовий кут для пелюсток квітки
starting_angle = 360 / 7

# лічильники правильних та неправильних слів
count_right = 0
count_wrong = 0

speed(0)
# список слів для гри
words = ["привіт"]
# випадкове слово для старту гри
word = choice(words)

# малюємо завдання
write_ask(word)
# малюємо квітку
draw_flower(colors)

# ігровий цикл
while True:
    # запитуємо літеру у гравця
    letter = input("Введіть літеру:")
    # первіряємо чи є така літера у слові
    if letter in word:
        # малюємо правильну/ні літери ТА рахуємо їх кількіст у слові
        c = write_right(letter, word)
        # збільшуємо лічильник вріних літер
        count_right += c
    # якщо літери немає у слові
    else:
        # малюємо неправильну літеру
        start(x_wrong, y_wrong)
        x_wrong += 45
        write_wrong(letter)
        # зібльшуємо лічильник неправильних літер
        count_wrong += 1
        # ЗАПАМ'ЯТАТИ колір пелюстки
        col = colors[count_wrong - 1]
        # ЗАМІНИТИ цей колір на білий
        colors[count_wrong - 1] = "white"
        # малюємо квітку заново та впавшу пелюстку
        draw_down_petal(colors, col)

    # перевірка програшу
    if count_wrong == 7:
        end_game("red", "Ти програв :(")
        break
    # перевірка виграшу
    if count_right == len(word):
        end_game("blue", "Ти виграв!")
        break

done()
