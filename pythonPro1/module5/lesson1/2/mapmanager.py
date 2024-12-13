class Mapmanager():
    """ Керування мапою """

    def __init__(self):
        self.model = 'block'  # модель кубика лежить у файлі block.egg
        # # використовуються такі текстури:
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)  # rgba

        # створюємо основний вузол мапи:
        self.startNew()
        # створюємо будівельні блоки
        self.addBlock((0, 10, 0))

    def startNew(self):
        """створює основу для нової мапи"""
        self.land = render.attachNewNode("Land")  # вузол, до якого прив'язані всі блоки мапи

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        # self.block.setColor(self.color)
        self.block.reparentTo(self.land)


