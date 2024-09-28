from memo_card_layout import (
   app, layout_card,
   lb_Question, lb_Correct, lb_Result,
   rbtn_1, rbtn_2, rbtn_3, rbtn_4,
   btn_OK, show_question, show_result
)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # перемішуватимемо відповіді у картці питання


card_width, card_height = 600, 500 # початкові розміри вікна "картка"
text_wrong = 'Неправильно'
text_correct = 'Правильно'


# у цій версії напишемо в коді одне запитання та відповіді до нього
# відповідні змінні поля майбутнього об'єкта "form" (тобто. анкета)
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'


# Тепер нам потрібно показати ці дані,
# причому відповіді розподілити випадково між радіокнопками, і пам'ятати кнопку з правильною відповіддю.
# Для цього створимо набір посилань на радіокнопки та перемішаємо його
