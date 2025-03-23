from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from panda3d.core import *
from direct.actor.Actor import Actor


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.camLens.setFov(90)

        self.city = self.loader.loadModel("CityPack.fbx")
        self.city.reparentTo(self.render)
        house_texture = self.loader.loadTexture("textures/Palette.jpeg")
        self.city.setTexture(house_texture, 1)

        self.city.setHpr(0, 90, 0)
        self.city.setScale(0.2)
        self.city.setPos(-2, 25, -3)

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.01)
        self.pandaActor.setPos(-2, 75, -25)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        self.move_speed = 30
        self.turn_speed = 75

        self.key_map = {"forward": False, "backward": False, "left": False, "right": False}

        self.accept("arrow_up", self.update_key_map, ["forward", True])
        self.accept("arrow_up-up", self.update_key_map, ["forward", False])

        self.accept("arrow_left", self.update_key_map, ["left", True])
        self.accept("arrow_left-up", self.update_key_map, ["left", False])

        self.taskMgr.add(self.update, "update")

    def update_key_map(self, key,value):
        self.key_map[key] = value
        print(key, value)

    def update(self, task):
        dt = globalClock.getDt()
        if self.key_map["forward"]:
            self.pandaActor.setY(self.pandaActor, -self.move_speed)
        if self.key_map["backward"]:
            self.pandaActor.setY(self.pandaActor, self.move_speed)
        if self.key_map["left"]:
            self.pandaActor.setH(self.pandaActor.getH()+self.turn_speed*dt)
        if self.key_map["right"]:
            self.pandaActor.setH(self.pandaActor.getH() - self.turn_speed * dt)

        cam_offset = Vec3(0, -40,40)
        self.camera.setPos(self.pandaActor.getPos()+cam_offset)
        self.camera.lookAt(self.pandaActor.getPos())
        return task.cont


game = Game()
game.run()
