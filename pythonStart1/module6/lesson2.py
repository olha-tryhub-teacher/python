#Підключення потрібних модулів
import pygame
from random import randint
pygame.init()


#створення вікна гри
clock = pygame.time.Clock()
back = (255,212,232)#колір фону (background)
mw = pygame.display.set_mode((500,500))#Вікно програми (main window)
mw.fill(back)


#кольори
BLACK = (0,0,0)
LIGHT_BLUE = (255,129,157)


class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):

    #запам'ятовуємо прямокутник:
        self.rect = pygame.Rect(x, y, width, height)
    # колір заливки - або переданий параметр, або загальний колір тла
        self.fill_color = color
        self.titles = []


    #додати текст до списку можливих написів
    def add_text(self, text):
        self.titles.append(text)


    #Встановити текст
    def set_text(self, number=0, fsize=20, text_color=BLACK):
        self.text = self.titles[number]
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)



    #Опис прямокутника з текстом
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))


#створення карток
quest_card = TextArea(120,100,300,70, LIGHT_BLUE)
quest_card.add_text('Питання')
quest_card.add_text('Що вивчаєш в Логіці?')
quest_card.add_text('Якою мовою говорять у Франції?')
quest_card.add_text('Що росте на яблуні?')
quest_card.add_text('Що падає з неба під час дощу?')
quest_card.add_text('Що їдять на вечерю?')
quest_card.set_text(0,75)
ans_card = TextArea(120,240,290,70, LIGHT_BLUE)
ans_card.add_text('Відповідь')
ans_card.add_text('Python')
ans_card.add_text('Французька')
ans_card.add_text('Яблука')
ans_card.add_text('Краплі дощу')
ans_card.add_text('Лазанью з грибами')
ans_card.set_text(0,75)
quest_card.draw(10,10)
ans_card.draw(10,10)


while 1:
    pygame.display.update()# оновлює екран, відображаючи всі зміни, внесені на поверхню.
    for event in pygame.event.get(): # це цикл, який обробляє всі події в черзі подій Pygame
        if event.type == pygame.KEYDOWN: # чи була подія натискання клавіші на клавіатурі
            if event.key == pygame.K_q: # чи була натиснута клавіша 'Q'
                num = randint(1, len(quest_card.titles) - 1)
                quest_card.set_text(num, 30)
                quest_card.draw(10, 25)

            if event.key == pygame.K_a:
                num = randint (1, len(ans_card.titles) - 1)
                ans_card.set_text(num, 30)
                ans_card.draw(10, 25)
    clock.tick(40)
