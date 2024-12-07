import pygame
from random import randint

pygame.init()

back = (200, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((500, 500))  # Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

game_over = False

coins = 0
monsters_smashed = 0
is_jump = False
jump_count = 15  # Початковий рахунок для стрибка
speed = 8

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

# клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        # self.image = pygame.transform.smoothscale(img, (width, height))

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area): # прямокутник із написом
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0): # відмалювання прямокутника із текстом
        self.fill() # відмальовуємо
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) # додаємо текст

background1 = Picture("backkground.png", 0, 0, 500, 350)
background2 = Picture("backkground.png", 500, 0, 500, 350)
backgrounds = [background1, background2]

mario = Picture("mario1.png", 50, 235, 80, 100)
coin = Picture("coin.png", 500, randint(100, 220), 40, 50)
mushroom_monster = Picture("mushroom.png", randint(500, 700), 270, 50, 50)

# створення написів
coins_text = Label(10, 10, 100, 50, (146,146,253))
monsters_text = Label(10, 50, 100, 50, (146,146,253))
game_over_text = Label(0, 0, 500, 500, (255,87,34))
game_over_text.set_text("GAME OVER", 60, (0, 0, 0))


while not game_over:
    # рух фону
    for bg in backgrounds:
        bg.rect.x -= speed
        bg.draw()
        if bg.rect.x < -500:
            bg.rect.x = 500

    # text
    coins_text.set_text("Coins collected: " + str(coins), 40, (255, 255, 255))
    coins_text.draw(0,0)
    monsters_text.set_text("Monsters smashed: " + str(monsters_smashed), 40, (255, 255, 255))
    monsters_text.draw(0,0)

    # рух монетки
    coin.rect.x -= speed
    coin.draw()

    # рух монстра
    mushroom_monster.rect.x -= speed
    mushroom_monster.draw()

    mario.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jump:
                is_jump = True
                jump_count = 15  # Починаємо стрибок
                mario = Picture("mario2.png", 50, 235, 100, 90)
                
        
    if is_jump:
        if jump_count > 0:  # Підйом
            mario.rect.y -= jump_count
            jump_count -= 1
        elif jump_count > -15:  # Спуск
            mario.rect.y -= jump_count
            jump_count -= 1
        else:  # Завершення стрибка
            is_jump = False
            mario = Picture("mario1.png", 50, 235, 80, 100)
            
    # зарахування монетки
    if coin.rect.colliderect(mario.rect):
        coin.rect.x = 550
        coin.rect.y = randint(100, 220)
        coins += 1
        print("всього монеток", coins)
    if coin.rect.x < -20:
        coin.rect.x = 550
        coin.rect.y = randint(100, 220)

    # респавн монстра
    if mushroom_monster.rect.x < -70:
        mushroom_monster.rect.x = randint(500, 700)

    # зіткнення з монстром
    if mushroom_monster.rect.colliderect(mario.rect):
        if is_jump: # якщо ми в прижку то вбиваємо монстра
            mushroom_monster.rect.x = randint(500, 700)
            monsters_smashed += 1
        else:
            game_over = True
            game_over_text.draw(100, 100)

            coins_text = Label(100, 160, 100, 50, (255,87,34))
            coins_text.set_text("Coins collected: " + str(coins), 40, (0, 0, 0))
            coins_text.draw(0,0)

            monsters_text = Label(100, 200, 100, 50, (255,87,34))
            monsters_text.set_text("Monsters smashed: " + str(monsters_smashed), 40, (0, 0, 0))
            monsters_text.draw(0,0)

            print("GAME OVER")
            

    
    pygame.display.update()
    clock.tick(40)
pygame.display.update()


