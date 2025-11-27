# підключення pygame
import pygame
from random import randint

# кольори
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 50
SPEED = 5
# налаштування Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

img_player = pygame.image.load("DinoRun1.png")

img_cactus = pygame.image.load("SmallCactus1.png")
img_cloud = pygame.image.load("Cloud.png")
img_ground = pygame.image.load("Track.png")


class Object:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = pygame.Rect(  # один рядок
            x, y, self.img.get_width(),  # один рядок
            self.img.get_height())  # один рядок

    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))

# клас гравця з керуванням
class Player(Object):
    def __init__(self, x, y):
        super().__init__(x, y, img_player)
        self.max_y = y
        self.velocity = 0
        self.GRAVITY = 0.7
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


class MovingObject(Object):
    def update(self):
        self.rect.left -= SPEED
        if self.rect.right < 0:
            self.rect.x = randint(600, 1000)


# кактус, що рухаються ліворуч
class Cactus(MovingObject):
    def __init__(self):
        x = randint(600, 1000)
        super().__init__(x, 400, img_cactus)


# хмара
class Cloud(MovingObject):
    def __init__(self):
        x = randint(500, 1000)
        y = randint(80, 200)
        super().__init__(x, y, img_cloud)

    def update(self):
        if self.rect.right <= 0:
            self.rect.y = randint(50, 300)
        super().update()


# реалізація переміщення та видалення об'єктів, що не взаємодіють з гравцем
class Enviroment(Object):
    def __init__(self, x, y):
        super().__init__(x, y, img_ground)
        self.cloud = Cloud()
        self.cactus = Cactus()

    def update(self):
        self.rect.left -= SPEED
        if self.rect.right <= 500:
            self.rect.left = 0

        self.cloud.update()
        self.cactus.update()

    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))
        self.cloud.draw(screen)
        self.cactus.draw(screen)


#################################
# створення годинника
clock = pygame.time.Clock()
running = True

# ігрові об'єкти та ігровий цикл
player = Player(100, 380)
enviroment = Enviroment(0, 460)

while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливка екрана кольором, відображення прямокутників
    screen.fill(WHITE)

    player.update()
    enviroment.update()
    player.draw(screen)
    enviroment.draw(screen)


    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
