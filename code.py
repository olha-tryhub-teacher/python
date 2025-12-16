
class Player(Sprite):
    def __init__(self, x, y, image_base):
        super().__init__(x, y, image_base)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.left -= 8
        if keys[pg.K_RIGHT]:
            self.rect.left += 8

