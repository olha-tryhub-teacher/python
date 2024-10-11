# 1.3

users = ['max123', 'sweet_girl', 'funIvan', 'crazy.cat']
#сортування списку учнів
users.sort()
#всього учнів
amount_users = len(users)
#гарний друк списку учнів
i = 1
print('Список користувачів:')
for user in users:
   print(i, '-', user)
   i += 1
print('Всього користувачів:', amount_users)

# 1.4
games = ['dota 2', 'cs go', 'warface', 'minecraft']
searching = input('Запит:')
searching = searching.lower()
#допиши програму
if searching in games:
    print("Запит знайдено у побажаннях")
else:
    print("Такого побажання не існує")

# 1.5
games = list()
game = input("Задай ім'я гри (0 - зупинити запит)").lower()
while game != "0":
    if game not in games:
        games.append(game)
    else:
        print("Ця гра вже записана")

    game = input("Задай ім'я гри (0 - зупинити запит)").lower()

games.sort()
print("Список ігор:", games)


# 1.6

# функція підрахунку кількості однакових оцінок
def number_of_ratings(list_rating, number):
    count = 0
    for el in list_rating:
        if el == number:
            count += 1
    return count

list_of_ratings = []
rating = int(input("Введи оцінку (0 - зупинити роботу програми)"))


while rating != 0:
    if rating >= 1 and rating <= 5:
        list_of_ratings.append(rating)
    rating = int(input("Введи оцінку (0 - зупинити роботу програми)"))

# кількість оцінок 5, 4, 3
five = number_of_ratings(list_of_ratings, 5)
four = number_of_ratings(list_of_ratings, 4)
three = number_of_ratings(list_of_ratings, 3)
# загальний рейтинг
all_rating = (five + four + three)/len(list_of_ratings) * 100


print("Список оцінок:", list_of_ratings)
print("Успішність:", all_rating)

2.5
def print_students(print_list):
    print("Список класу:")
    print_list.sort()
    for i in range(len(print_list)):
        print(i+1,"-",print_list[i])


# поточний список студентів
my_students = ['Абрикосов', 'Воробйова', 'Лісіцин', 'Олійник', 'Щукіна']
print_students(my_students)
# додавання нового студента
name= input("Введіть прізвище студента:")
my_students.append(name)
# друк оновленого списку
print_students(my_students)