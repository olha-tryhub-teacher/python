
'''клас прямокутник'''

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямокутник
        self.fill_color = color

    def color(self, new_color): # зберігаємо новий колір
        self.fill_color = new_color

    def fill(self): # відмальовуємо прямокутник
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обведення існуючого прямокутника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

'''клас напис'''

class Label(Area): # прямокутник із написом
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0): # відмалювання прямокутника із текстом
        self.fill() # відмальовуємо
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) # додаємо текст
