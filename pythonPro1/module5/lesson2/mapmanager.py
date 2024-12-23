class Mapmanager:
    """Управління карткою"""

    def __init__(self):
        self.model = 'block'  # модель кубика лежить у файлі block.egg
        # використовуються такі текстури:
        self.texture = 'anime.png'
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ]  # rgba
        # створюємо основний вузол картки:
        self.startNew()
        # self.addBlock((0, 10, 0))

    def startNew(self):
        """Створює основу для нової карти"""
        self.land = render.attachNewNode("Land")  # вузол, до якого прив'язані всі блоки картки

    def getColor(self, z):
        """Повертає колір для заданого рівня висоти"""
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def addBlock(self, position):
        """Створює будівельні блоки"""
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        """Обнуляє карту"""
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        """Створює карту землі з текстового файлу, повертає її розміри"""
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1
