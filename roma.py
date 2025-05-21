class BonusShip(GameSprite):
    def __init__(self, img, size_x, size_y, speed):
        side = randint(0, 1)
        y = randint(50, win_height // 2 - 50)
        if side == 0:
            x = -size_x
            self.direction = 1  # рух праворуч
        else:
            x = win_width
            self.direction = -1  # рух ліворуч
        super().__init__(img, x, y, size_x, size_y, speed)

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > win_width:
            self.kill()
