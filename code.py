from turtle import *
from art import *
from guess_word import *
from random import randint
## Список кольорів пелюсток
colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f","#e74c3c","#5dade2"]


# координати квітки
x_start,y_start = 400,-150
# координати завдання
x_ask,y_ask = -170,100
# координати для відображення невірних літер
x_wrong, y_rong = -170, 50


# радіус пелюстки та листочків
r = 95
# стартовий кут для пелюсток квітки
starting_angle = 360/7


# лічильники вірних та невірних слів
count_right = 0
count_wrong = 0




speed(0)
# список слів для гри
words = []
# випадкове слово для старту гри
word = "gh"


# малюємо завдання
write_ask(word)
# малюємо квітку
draw_flower()


# ігровий цикл
while True:
    # запитуємо літеру у гравця
    letter = input("Введіть літеру:")
    # первіряємо чи є така літера у слові
    if letter in word:
        # малюємо вірну/ні літери ТА рахуємо їх кількіст у слові
        c = write_right(letter)
        # збільшуємо лічильник вріних літер
        count_right += c
    # якщо літери немає у слові    
    else:
        # малюємо невірну літеру
        start(x_wrong,y_wrong)
        x_Wrong += 45
        write_Wrong(letter)
        # зібльшуємо лічильник невірних літер
        count_wrong += 1
        # ЗАПАМ'ЯТАТИ колір пелюстки
        col = colors[count_wrong-1]
        # ЗАМІНИТИ цей колір на білий
        colors[count_wrong-1] = "white"
        # малюємо квітку заново та впавшу пелюстку
        draw_down_petal(col)
       
    # перевірка програшу    
    if count_wrong == 7:
        end_game("red","Ти програв :(")
        break
    # перевірка виграшу
    if count_right == len(word):
        end_game("blue","Ти виграв!")
        break
