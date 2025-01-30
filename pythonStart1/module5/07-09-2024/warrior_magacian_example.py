from time import sleep

class Hero():
    #конструктор класу
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health #число
        self.armor = armor #рядок
    #друк параметрів персонажа
    def print_info(self):
        print("Рівень здоров'я:", self.health)
        print("Клас броні:", self.armor)

#далі запрограмуй класи-спадкоємці суперкласу Hero

class Warrior(Hero):
    
    def hello(self):
        print("-> НОВИЙ ГЕРОЙ. Верхом на коні з'явився бравий воїн на ім'я",self.name)
        self.print_info()
        sleep(4)


    def attack(self,enemy):
        print('-> УДАР! Хоробрий воїн',self.name,'атакує', enemy.name,'мечем!')
        enemy.armor -=15 #сила удару для класу Воїн
        if enemy.armor <0:
            enemy.health += enemy.armor
            enemy.armor =0
        print('Страшний удар обрушився на супротивника.\nТепер його броня: '+
        str(enemy.armor) +", а рівень здоров'я: "+str(enemy.health) +'\n')
        sleep(5)


class Magician(Hero):
    def hello(self):
        print("-> НОВИЙ ГЕРОЙ. Звідки не візьмись з'явився майстерний чарівник",self.name)
        self.print_info()
        sleep(4)


    def attack(self,enemy):
        print('-> УДАР! Спритний маг',self.name,'накладає заклинання на', enemy.name)
        enemy.armor -=35 #сила удару для класу Маг
        if enemy.armor <0:
            enemy.health += enemy.armor
            enemy.armor =0
        print('Складне заклинання приголомшило супротивника.\nТепер його броня: '+
        str(enemy.armor) +", а рівень здоров'я: "+str(enemy.health) +'\n')
        sleep(5)




warrior1 = Warrior('Henry',100,50)
warrior1.hello()


magician1 = Magician('Luke', 50, 20)
magician1.hello()


warrior1.attack(magician1)
magician1.attack(warrior1)
