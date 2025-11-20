    def update(self):
        if self.rect.right <= 0:
            self.rect.y = randint(50, 300)
        super().update()
