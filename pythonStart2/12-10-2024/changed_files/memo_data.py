from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

new_quest_templ = 'Нове питання'  # така строка буде встановлюватися за замовчуванням для нових питань
new_answer_templ = 'Нова відповідь'  # те саме для відповідей

text_wrong = 'Неправильно'
text_correct = 'Правильно'

class Form():
    ''' зберігає інформацію про одне питання'''

    def __init__(self, question=new_quest_templ, answer=new_answer_templ,
                       wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question  # питання
        self.answer = answer  # правильна відповідь
        self.wrong_answer1 = wrong_answer1  # вважаємо, що завжди пишеться три неправильних варіанти
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True  # чи продовжувати ставити це питання?
        self.attempts = 0  # скільки разів це питання ставилося
        self.correct = 0  # кількість правильних відповідей
    def got_right(self):
        ''' змінює статистику при отриманні правильної відповіді '''
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        ''' змінює статистику при отриманні неправильної відповіді '''
        self.attempts += 1

class FormView():
    ''' відповідає за відображення даних питання на екрані '''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор отримує та запам'ятовує об'єкт з даними та віджети, що відповідають полям форми
        self.frm_model = frm_model  # може отримати і None - нічого страшного не станеться,
                                    # але для методу show потрібно буде попередньо оновити дані методом change
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
    def change(self, frm_model):
        ''' оновлення даних, вже пов'язаних з інтерфейсом '''
        self.frm_model = frm_model
    def show(self):
        ''' виводить на екран усі дані з об'єкта '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

class FormEdit(FormView):
    ''' використовується для редагування форми: встановлює обробники подій, які зберігають текст '''
    def save_question(self):
        ''' зберігає текст питання '''
        self.frm_model.question = self.question.text()  # копіюємо дані з віджета в об'єкт
    def save_answer(self):
        ''' зберігає текст правильної відповіді '''
        self.frm_model.answer = self.answer.text()  # копіюємо дані з віджета в об'єкт
    def save_wrong(self):
        ''' зберігає всі неправильні відповіді
        (якщо в наступній версії програми кількість неправильних відповідей стане змінною
        і вони вводитимуться у списку, можна буде змінити цей метод) '''
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()
    def set_connects(self):
        ''' встановлює обробники подій у віджетах, щоб зберігати дані '''
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong)
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # перевизначимо конструктор, щоб не викликати вручну set_connects (діти можуть викликати вручну)
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()

class AnswerCheck(FormView):
    ''' перевіряє, чи обрана правильна відповідь (якщо відповіді відображаються через чекбокси) '''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        ''' запам'ятовує всі властивості. showed_answer - це віджет, де буде записано правильну відповідь (показується пізніше)
        result - це віджет, куди буде записано text_correct або text_wrong'''
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result
    def check(self):
        ''' відповідь заноситься до статистики, але перемикання на формі не відбувається:
        цей клас нічого не знає про панелі на формі '''
        if self.answer.isChecked():
            # відповідь правильна, запишемо та відобразимо в статистиці
            self.result.setText(text_correct)  # напис "правильно" або "неправильно"
            self.showed_answer.setText(self.frm_model.answer)  # пишемо текст відповіді в відповідному віджеті
            self.frm_model.got_right()  # оновлюємо статистику, додавши один правильний відповідь
        else:
            # відповідь неправильна, запишемо та відобразимо в статистиці
            self.result.setText(text_wrong)  # напис "правильно" або "неправильно"
            self.showed_answer.setText(self.frm_model.answer)  # пишемо текст відповіді в відповідному віджеті
            self.frm_model.got_wrong()  # оновлюємо статистику, додавши неправильну відповідь

class FormListModel(QAbstractListModel):
    ''' список об'єктів типу Form і список активних питань для відображення на екрані '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []
    def rowCount(self, index):
        ''' кількість елементів для показу: обов'язковий метод для моделі, пов'язаної з віджетом "список" '''
        return len(self.form_list)
    def data(self, index, role):
        ''' обов'язковий метод для моделі: які дані вона надає на запит від інтерфейсу '''
        if role == Qt.DisplayRole:
            # інтерфейс хоче намалювати цей рядок, дамо йому текст питання для відображення
            form = self.form_list[index.row()]
            return form.question
    def insertRows(self, parent=QModelIndex()):
        ''' цей метод викликається для вставки нових даних у список об'єктів;
        генерується та вставляється одне порожнє питання '''
        position = len(self.form_list)  # вставляємо в кінець, це треба повідомити:
        self.beginInsertRows(parent, position, position)  # вставка даних повинна бути після цього виклику і перед endInsertRows()
        self.form_list.append(Form())  # додали нове питання до списку даних
        self.endInsertRows()  # завершили вставку (тепер можна продовжувати працювати з моделлю)
        QModelIndex()
        return True  # повідомляємо, що все пройшло добре
    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартний метод для видалення рядків - після видалення рядок автоматично зникає з екрану '''
        self.beginRemoveRows(parent, position, position)  # повідомляємо, що будемо видаляти рядок
        self.form_list.pop(position)  # видаляємо елемент зі списку на позиції position
        self.endRemoveRows()  # завершили видалення
        return True  # все добре
    def random_question(self):
        ''' Повертає випадкове питання '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]

def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    '''повертає новий екземпляр класу AnswerCheck,
    з випадковим питанням та випадковим розподілом відповідей по віджетах'''
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card
