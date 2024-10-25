import pygame
import time
pygame.init()

'''створюємо вікно програми'''

back = (200, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((500, 500))  # Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

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

YELLOW = (255, 255, 0) # кольори для прямокутників
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)

cards = [] # список об'єктів прямокутників
num_cards = 4

x = 70 # звідки починаємо малювати прямокутники

for i in range(num_cards): # створюємо картки, ще не малюємо
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card) # створили і додали у список
    x = x + 100

while True: # створюємо ігровий цикл
    for card in cards:
        card.draw(10, 30) # відмальовуємо прямокутники

    pygame.display.update() # оновлюємо екран
    clock.tick(40) # чекаємо 40 мілісекунд
