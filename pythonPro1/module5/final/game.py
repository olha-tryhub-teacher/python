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

        # Завантажити модель
        model = self.loader.loadModel('models/backgrounds/sky_sphere')
        # Додати модель у сцену
        model.reparentTo(self.render)

        base_texture = loader.loadTexture('models/backgrounds/img.png')
        model.setTexture(base_texture)

        # model.setColor((1, 1, 1, 1))

        # Налаштувати позицію, масштаб і обертання
        model.setPos(0, 0, 0)
        model.setScale(50, 50, 50)
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
