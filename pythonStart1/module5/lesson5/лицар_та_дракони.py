####### 111111

class Hero():
    def __init__(self, name, hp, armor, power, weapon):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.weapon = weapon
    
    def print_info(self):
        print(f"""
        Привітай героя -> {self.name}
        Рівень здоров'я: {self.hp}
        Клас броні: {self.armor}
        Сила удару: {self.power} 
        Зброя: {self.weapon}""")
    
    def strike(self, other):
        if other.hp + other.armor <= self.power:
            other.hp = 0
            print(f"Героя на ім'я {other.name} убито героєм на ім'я {self.name}")
        else:
            other.hp = other.hp - self.power + other.armor
            print(f"Герой на ім'я {other.name} отримує удару від {self.name}")
        print("Залишок здоров'я:")
        print(self.name, "->", self.hp)
        print(other.name, "->", other.hp)
    
    def fight(self, other):
        print("Сутичка почалась!")
        while self.hp != 0 and other.hp != 0:
            self.strike(other)
            other.strike(self)
        
        if self.hp == other.hp:
            print("Нічия!")
        elif self.hp > other.hp:
            print("У сутичці переміг герой", self.name)
        else:
            print("У сутичці переміг герой", other.name)


####### 22222222
from hero import Hero
#          name   hp  armor power weapon
h1 = Hero("Пудж", 3250, 50, 450, "Хук")
h2 = Hero("Емз", 3500, 60, 550, "Перцовка")
# h3 = Hero("FV4005", 2900, 90, 700, "Фугас")
# h4 = Hero("Річард", 5000, 500, 500, "АК47")

h1.print_info()
h2.print_info()
# h3.print_info()
# h4.print_info()

h2.fight(h1)
