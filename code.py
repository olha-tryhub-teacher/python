class TextLabel:
    def __init__(self, x, y, size=32, color=BLACK):
        self.x = x
        self.y = y
        self.color = color
        self.image = None
        self.font = pg.font.Font(None, size)

    def set_text(self, text):
        self.image = self.font.render(text, True, self.color)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

