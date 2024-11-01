import pygame
import time
############3
from random import randint# new import
################
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
    
    ###################
    def collidepoint(self, x, y): # new method
        return self.rect.collidepoint(x, y)
    ###################

'''клас напис'''

class Label(Area): # прямокутник із написом
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0): # відмалювання прямокутника із текстом
        self.fill() # відмальовуємо
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) # додаємо текст


# додаємо нові кольори
RED = (255, 0, 0)
GREEN = (0, 255, 51)
###############
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)

cards = [] # список об'єктів прямокутників
num_cards = 4

x = 70 # звідки починаємо малювати прямокутники

###############
wait = 0 #нова змінна для рахунку кадрів скільк ичекає картка
###############

for i in range(num_cards): # створюємо картки, ще не малюємо
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card) # створили і додали у список
    x = x + 100

while True: # створюємо ігровий цикл
    # for card in cards:
    #     card.draw(10, 30) # відмальовуємо прямокутники

    #####################
    if wait == 0:
        #переносимо напис:
        wait = 30 #стільки тиків напис буде на одному місці
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i == click - 1: # якщо дійшли до картки потрібного номеру, то малюємо на ній клік
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    #на кожному тику перевіряємо клік::
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos # отримуємо координати кліку миші
            for i in range(num_cards):
                #шукаємо, в яку карту потрапив клік
                    if cards[i].collidepoint(x,y):
                        if i == click - 1: #якщо на карті є напис - перефарбовуємо в зелений плюс очко
                            cards[i].color(GREEN)
                        else: #інакше перефарбовуємо в червоний, мінус очко
                            cards[i].color(RED)
                        cards[i].fill()
    ####################################

    pygame.display.update() # оновлюємо екран
    clock.tick(40) # чекаємо 40 мілісекунд
