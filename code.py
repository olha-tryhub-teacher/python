class Animal:
    def __init__(self, n, e):
        self.name = n
        self.energy = e
    
    def eat(self, food):
        self.energy += food.energy
        food.energy = 0
        print(f"{self.name} - {self.energy}")
        

class Food:
    def __init__(self, n, e):
        self.name = n
        self.energy = e
