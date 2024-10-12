# class Question():
#     def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
#         self.question = question # питання
#         self.answer = answer # правильну відповідь
#         self.wrong_answer1 = wrong_answer1 
#   # вважаємо, що завжди пишеться три невірні варіанти
#         self.wrong_answer2 = wrong_answer2  
#         self.wrong_answer3 = wrong_answer3 
#     def got_right(self):
#         print("Це правильна відповідь!")
#     def got_wrong(self):
#         print("Відповідь неправильна")


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question # вопрос
        self.answer = answer # правильну відповідь
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2  
        self.wrong_answer3 = wrong_answer3 
        self.correct = 0
        self.attempts = 0
    def got_right(self):
        self.correct += 1
        self.attempts += 1
        print("Це правильна відповідь!")
    def got_wrong(self):
        self.attempts += 1
        print("Відповідь неправильна")