

class Sprite:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = pg.Rect(x, y, self.image.get_width(), self.image.get_height())

    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.left, self.rect.top))
