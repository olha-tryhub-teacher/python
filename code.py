class Ball(Sprite):
    def __init__(self, x, y, image, velocity):
        super().__init__(x, y, image)
        self.SPEED = velocity
        self.velocityx = velocity
        self.velocityy = -velocity

    def update(self):
        self.rect.left += self.velocityx
        self.rect.top += self.velocityy

        # Відскок від стінок та верху екрана
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocityx = -self.velocityx
        if self.rect.top < 0:
            self.velocityy = self.SPEED

    def change_velocity(self, player):
        self.velocityy = -self.SPEED
