# кактус, що рухаються ліворуч
class Cactus(MovingObject):
    def __init__(self):
        x = randint(600, 1000)
        super().__init__(x, 400, img_cactus)


# хмара
class Cloud(MovingObject):
    def __init__(self):
        x = randint(500, 1000)
        y = randint(80, 200)
        super().__init__(x, y, img_cloud)
