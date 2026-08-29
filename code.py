from time import sleep


# Клас Hero — опис героя з характеристиками та поведінкою
class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name  # Ім'я героя
        self.health = health  # Рівень здоров’я
        self.armor = armor  # Клас броні (захист)
        self.power = power  # Сила атаки
        self.weapon = weapon  # Зброя героя

    # Метод виводу інформації про героя
    def print_info(self):
        print(f'Привітайте героя {self.name}')
        print(f'Рівень здоров’я: {self.health}')
        print(f'Броня: {self.armor}')
        print(f'Сила: {self.power}')
        print(f'Має зброю: {self.weapon}')

    # Метод атаки героя по ворогу
    def strike(self, enemy):
        print(f"Герой {self.name} атакує {enemy.name} з силою {self.power}, використовуючи {self.weapon}")
        sleep(1)  # Затримка для ефекту драматизації

        enemy.armor -= self.power  # Зменшуємо броню ворога на силу атаки
        if enemy.armor < 0:
            # Якщо броня опустилась нижче 0, решта шкоди йде по здоров’ю
            enemy.health += enemy.armor  # enemy.armor - від’ємне число, тому додаємо
            enemy.armor = 0  # Броня не може бути від’ємною

        print(f"{enemy.name} похитнувся.")
        sleep(1)
        print(f"Клас броні впав до {enemy.armor}, рівень здоров’я до {enemy.health}")
        sleep(1)


# Функція бою між двома героями
def battle(fighter1, fighter2):
    print(f"{fighter1.name} зустрічає {fighter2.name}")
    while True:
        fighter1.strike(fighter2)  # Перший герой атакує другого
        if fighter2.health <= 0:  # Якщо другий герой програв (здоров’я <= 0)
            print(f"*****{fighter2.name} програв!******")
            return fighter1  # Перший герой переможець

        fighter2.strike(fighter1)  # Другий герой атакує першого
        if fighter1.health <= 0:  # Якщо перший герой програв
            print(f"*****{fighter1.name} програв!******")
            return fighter2  # Другий герой переможець

        print("********************")
        sleep(2)  # Пауза перед наступним раундом


# Створення героїв
knight = Hero("Річард", 50, 25, 20, "меч")
robber = Hero("Генрі", 20, 15, 15, "лук")
dragon = Hero("Лазурний", 55, 32, 21, "вогонь")

print("Леді та джентельмени, схоже, скоро буде битва!")
print("Переможе сьогодні сильніший\n")

# Виведення інформації про кожного героя
for hero in (knight, robber, dragon):
    hero.print_info()
    print()

print("********************")
print("Лицар починає шлях...")
print("********************")
sleep(1)

# Перша битва: лицар проти розбійника
winner = battle(knight, robber)

if winner == knight:
    print("******Лицар помножив свою силу та броню********")
    knight.armor *= 2  # Подвоєння броні лицаря після перемоги
    knight.power *= 2  # Подвоєння сили лицаря після перемоги
    print("********************")
    sleep(2)

    print(f"Лицар {knight.name} зустрічає Дракона {dragon.name} та йде бій")
    winner = battle(knight, dragon)  # Друга битва: лицар проти дракона

    print("********************")
    sleep(2)

    if winner == knight:
        print("Лицар переміг!")
    else:
        print("Лицар програв :(")
else:
    print("Лицар програв :(")
