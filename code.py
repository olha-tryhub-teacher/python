# клас для об'єктів-спрайтів
class Sprite:
    def __init__(self, coord, color):
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = pygame.Rect(coord, (100, 100))
        self.dx = 5

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > 500:
            self.dx = -5  # змінити напрямок руху вліво
        elif self.rect.left < 0:
            self.dx = 5   # змінити напрямок руху вправо


    def draw(self, surface):
        # відображення зображення (image) на екрані
        surface.blit(self.image, (self.rect.x, self.rect.y))
