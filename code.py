import turtle as t
from time import sleep


LEVELS = [
    [
        (-80, -120, -200, 0, "Сідней", True),
        (-80, 120, 0, 0, "Берлін", False),
        (80, 120, 0, 0, "Рим", False),
        (80, -120, 0, 0, "Київ", False),
    ],
    [
        (-80, 120, 0, 0, "Атлантичний", False),
        (200, 0, 120, -120, "Китайський", True),
        (80, 120, 0, 0, "Індійський", False),
        (80, -120, 0, 0, "Тихий", False),
    ],
    [
        (-200, 120, 0, 0, "Python", False),
        (100, 120, 0, 0, "C++", False),
        (0, 0, 0, 200, "Mouse", True),
        (0, -120, 0, 0, "JavaAcript", False),
    ],
    [
        (-80, 120, 0, 0, "Cat", False),
        (80, 120, 0, 0, "Dog", False),
        (0, -120, 0, 0, "Mouse", False),
        (0, 200, 160, 40, "Shark", True),
    ],
    [
        (120, -120, -80, -120, "Head", True),
        (-120, -120, 0, 0, "CPU", False),
        (0, 0, 0, 0, "SSD", False),
        (150, 0, 0, 0, "RAM", False),
    ],
    [
        (-80, 120, 0, 0, "Red", False),
        (-120, 40, 0, 200, "Brawl", True),
        (80, 120, 0, 0, "Green", False),
        (100, 0, 0, 0, "Blue", False),
    ],
    [
        (-80, 120, 0, 0, "Train", False),
        (80, 120, 0, 0, "Car", False),
        (-200, 0, 200, 0, "Seat", True),
        (120, 0, 0, 0, "Rocket", False),
    ],
    [
        (-80, 120, 0, 0, "One", False),
        (80, 120, 0, 0, "Two", False),
        (80, -120, 0, 0, "Three", False),
        (160, 40, -120, 40, "Minus", True),
    ],
]
