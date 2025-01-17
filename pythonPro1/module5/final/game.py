from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, PointLight, AmbientLight
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand("land.txt")

        x, y = self.land.loadLand("land.txt")
        self.hero = Hero((x // 2, y // 2, 2), self.land)

        # Завантажити модель Bugatti
        model = self.loader.loadModel('bench.obj')
        # Додати модель у сцену
        model.reparentTo(self.render)

        base_texture = loader.loadTexture('benchTex.png')
        model.setTexture(base_texture, 1)

        # model.setColor((1, .75, .79, 1))

        # Налаштувати позицію, масштаб і обертання
        model.setPos(0, 0, 0)
        model.setScale(10, 10, 10)
        model.setHpr(90, 0, 0)

        base.camLens.setFov(90)

        self.setupLighting()

    def setupLighting(self):
        # Додати направлене світло
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setColor((1, 1, 1, 1))  # Біле світло
        directionalLightNP = self.render.attachNewNode(directionalLight)
        directionalLightNP.setHpr(-45, -45, 0)  # Кут освітлення
        self.render.setLight(directionalLightNP)

        # Додати розсіяне світло
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((0.6, 0.6, 0.6, 1))  # М'яке, тьмяне світло
        ambientLightNP = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNP)

        # Додати точкове світло (опціонально)
        pointLight = PointLight("pointLight")
        pointLight.setColor((1, 1, 1, 1))  # Біле світло
        pointLightNP = self.render.attachNewNode(pointLight)
        pointLightNP.setPos(10, 10, 15)  # Позиція світла
        self.render.setLight(pointLightNP)






game = Game()
game.run()
