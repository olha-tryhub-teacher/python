class Pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark


sum = 0
amount = 0
best_pupils = []

with open("pupils.txt", "r", encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))

        if data_pupil.mark == 5:
            best_pupils.append(data_pupil.surname)
        amount += 1
        sum += int(data_pupil.mark)


print("Середня оцінка:", (sum/amount), "\n\nКількість відмінників:", len(best_pupils))
