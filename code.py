class Object:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = pygame.Rect(  # один рядок
            x, y, self.img.get_width(),  # один рядок
            self.img.get_height())  # один рядок

    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))

class MovingObject(Object):
    def update(self):
        self.rect.left -= SPEED
        if self.rect.right < 0:
            self.rect.x = randint(600, 1000)
