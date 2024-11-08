from PyQt5.QtWidgets import QWidget
from random import shuffle # перемішуватимемо відповіді у картці питання

from memo_app import app
from memo_data import Form, FormView

from memo_main_layout import layout_main, btn_card, btn_form, wdgt_edit, wdgt_card
from memo_card_layout import (
    # app, layout_card, - це більше не треба!
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result
)
from memo_edit_layout import (txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
card_width, card_height = 600, 500 # початкові розміри вікна "картка"
# 🔽🔽 встановимо колір для написів
text_wrong = '''<font color="red">Неправильно</font>'''
text_correct = '''<font color="green">Правильно</font>'''

# 🔽🔽 Створимо об'єкт form замість змінних із даними
frm = Form('Як називається моб в майнкрафті, який взривається?', 'кріпер', 'золоте яблуко', 'стів', 'свиня')

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)  # перемішуємо варіанти відповідей
# 🔽🔽 пов'язуємо інформацію про питання із формою відповіді на питання
frm_card = FormView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])
# 🔽🔽 пов'язуємо інформаціюіз формою редагування питання
frm_edit = FormView(frm, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)

# 🔽🔽 цей метод нам тепер не треба
# def show_data():
#    ''' показує потрібну інформацію на екрані '''
#    # об'єднаємо у функцію схожі дії
#    lb_Question.setText(frm_question)
#    lb_Correct.setText(frm_right)
#    answer.setText(frm_right)
#    wrong_answer1.setText(frm_wrong1)
#    wrong_answer2.setText(frm_wrong2)
#    wrong_answer3.setText(frm_wrong3)

def check_result():
    ''' перевірка, чи правильна відповідь обрана
    якщо відповідь була обрана, то напис "правильно/неправильно" набуває потрібного
    значення і показується панель відповідей
    '''
    # 🔽🔽 додаємо frm_card
    correct = frm_card.answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
    if correct:
        # відповідь правильна, запишемо
        lb_Result.setText(text_correct) # надпись "верно" или "неверно"
        # 🔽🔽 треба дописати цей рядок, бо прибрали метод show_data
        lb_Correct.setText(frm_card.answer.text())
        show_result()
    else:
                    # 🔽🔽 додаємо frm_card             🔽🔽 додаємо frm_card                   🔽🔽 додаємо frm_card
        incorrect = frm_card.wrong_answer1.isChecked() or frm_card.wrong_answer2.isChecked() or frm_card.wrong_answer3.isChecked()
        if incorrect:
            # відповідь невірна, запишемо і відобразимо у статистиці
            lb_Result.setText(text_wrong) # "неправильно"
            # 🔽🔽 треба дописати цей рядок, бо прибрали метод show_data
            lb_Correct.setText(frm_card.answer.text())
            show_result()

def click_OK(self):
    # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
    if btn_OK.text() != 'Наступне питання':
        check_result()

# 🔽🔽 додаємо метод
def show_card():
    # показати питання
    wdgt_edit.hide()
    wdgt_card.show()

# 🔽🔽 додаємо метод
def show_form():
    # редагувати питання
    wdgt_card.hide()
    wdgt_edit.show()


win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_main)
# show_data() натомість використовуємо методи об'єктів, що пов'язують форми з даними:
# 🔽🔽
frm_card.show()
frm_edit.show()
show_question()
# 🔽🔽 показуємо картку для редагування
show_card()

# 🔽🔽 підєднуємо функції до кнопок
btn_card.clicked.connect(show_card)
btn_form.clicked.connect(show_form)
btn_OK.clicked.connect(click_OK)

win_card.show()
app.exec()
