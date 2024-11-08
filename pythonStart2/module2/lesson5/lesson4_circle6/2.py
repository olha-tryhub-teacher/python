from Question import *


Q1 = Question("Як звали Шевченка?", "Тарас", "Іван", "Марк", "Олег")
print(Q1.question)
print(Q1.answer, " ", Q1.wrong_answer1, " ", Q1.wrong_answer2, " ", Q1.wrong_answer3)
answer = input()


if answer == Q1.answer:
    Q1.got_right()
else:
    Q1.got_wrong()