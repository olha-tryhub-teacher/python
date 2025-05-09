import pygame

pygame.init()

'''СТВОРЕННЯ ВІКНА'''

back = (200, 255, 255)  # колір фону (background)
window = pygame.display.set_mode((500, 500))  # Вікно програми
window.fill(back)
clock = pygame.time.Clock()


#прапор закінчення гри⬅️
game_over = False

'''клас прямокутник'''


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямокутник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обведення існуючого прямокутника
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect): # новий метод для зіткнення⬅️
        return self.rect.colliderect(rect)


'''клас напис'''


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# клас для об'єктів-картинок⬅️
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename), (width, height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# ПРИКЛАД СТВОРЕННЯ ОБ'ЄКТІВ
ball = Picture('ball.png', 160, 200, 150, 150)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)


while not game_over:
    # ТУТ БУДЕ ІГРОВА ЛОГІКА

    
    pygame.display.update()
    clock.tick(40)

