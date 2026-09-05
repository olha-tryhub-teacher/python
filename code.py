class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Pupil(Human):
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = mark
    
    def info(self):
        super().info()
        print("Mark:", self.mark)
        

h1 = Human("OptimusPrime", 10)
h1.info()
