new_quest_templ = 'Нове питання' # такий рядок буде встановлюватись за умовчанням для нових питань
new_answer_templ = 'Нова відповідь' # теж для відповідей

class Form():
    ''' зберігає інформацію про одне питання '''
    def __init__(self, question=new_quest_templ, answer=new_answer_templ, 
                       wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question # питання
        self.answer = answer # правильна відповідь
        self.wrong_answer1 = wrong_answer1 # вважаємо, що завжди пишеться три невірні варіанти
        self.wrong_answer2 = wrong_answer2 # 
        self.wrong_answer3 = wrong_answer3 #
        self.is_active = True # чи продовжувати ставити це питання?
        self.attempts = 0 # скільки разів це питання ставилося
        self.correct = 0 # кількість вірних відповідей
    def got_right(self):
        ''' змінює статистику, отримавши правильну відповідь '''
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        ''' змінює статистику, отримавши неправильну відповідь '''
        self.attempts += 1

class FormView():
    ''' зіставляє дані та віджети для візуалізації питання
    цей клас і його спадкоємці схожі на те, що робить QDataWidgetMapper
     краще обійтися без додаткового абстрактного класу,
    а прописувати безпосередньо зв'язок з елементами нашої форми'''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор отримує та запам'ятовує об'єкт з даними та віджети, що відповідають полям питання
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
