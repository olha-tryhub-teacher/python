# клас гравця з керуванням
class Player(Object):
    def __init__(self, x, y):
        super().__init__(x, y, img_player)
        self.max_y = y
        self.velocity = 0
        self.GRAVITY = 0.007
        self.in_air = False

    # реалізація керування і гравітації
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.in_air:
            self.velocity = 15
            self.in_air = True

        if self.in_air:
            self.rect.top -= self.velocity
            self.velocity -= self.GRAVITY
            if self.rect.top >= self.max_y:
                self.in_air = False
                self.rect.top = self.max_y
