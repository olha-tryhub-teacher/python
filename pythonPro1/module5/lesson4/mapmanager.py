import math

class Mapmanager:
    """Керування карткою"""

    def __init__(self):
        self.model = 'block'  # модель кубика лежить у файлі block.egg
        # використовуються такі текстури:
        self.textures = [
            "textures/red.jpg",
            "textures/orange.jpg",
            "textures/pink.jpg",
            "textures/purple.jpg",
            "textures/blue.jpg",
            "textures/white.jpg",
        ]

        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ]  # rgba
        # створюємо основний вузол картки:
        self.startNew()
        # Додамо структуру даних для збереження блоків
        self.blocks = {}

    def startNew(self):
        """Створює основу для нової карти"""
        self.land = render.attachNewNode("Land")  # вузол, до якого прив'язані всі блоки картки
        self.blocks = {}  # Очищаємо список блоків

    def getColor(self, z):
        """Повертає колір для заданого рівня висоти"""
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def getTexture(self, z):
        """Повертає текстуру для заданого рівня висоти"""
        if z < len(self.textures):
            return self.textures[z]
        else:
            return self.textures[len(self.textures) - 1]

    def addBlock(self, position):
        """Створює будівельні блоки"""
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.getTexture(int(position[2]))))
        self.block.setPos(position)
        # self.color = self.getColor(int(position[2]))
        # self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        # Додаємо блок до списку блоків (позиція як ключ, блок як значення)
        self.blocks[position] = self.block

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
        return x, y

    def isBlockAt(self, position):
        return position in self.blocks

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while self.isBlockAt((round(x), round(y), round(z))):
            z += 1
        return (round(x), round(y), z)

    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= round(z) + 1:
            self.addBlock(new)

    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = round(x), round(y), round(z) - 1
        for block in self.findBlocks(pos):
            block.removeNode()

