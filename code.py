# реалізація переміщення та видалення об'єктів, що не взаємодіють з гравцем
class Enviroment(Object):
    def __init__(self, x, y):
        super().__init__(x, y, img_ground)
        self.cloud = Cloud()
        self.cactus = Cactus()

    def update(self):
        self.rect.left -= SPEED
        if self.rect.right <= 500:
            self.rect.left = 0

        self.cloud.update()
        self.cactus.update()

    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))
        self.cloud.draw(screen)
        self.cactus.draw(screen)
