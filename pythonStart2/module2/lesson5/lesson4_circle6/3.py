from Question2 import *


Q1 = Question("Як звали Шевченка?", "Тарас", "Іван", "Марк", "Олег")


for i in range(5):
    print(Q1.question)
    print(Q1.answer, " ", Q1.wrong_answer1, " ", Q1.wrong_answer2, " ", Q1.wrong_answer3)
    answer = input()
    if answer == Q1.answer:
        Q1.got_right()
    else:
        Q1.got_wrong()


print("Ви дали ", Q1.correct, " правильних відповідей з ", Q1.attempts)