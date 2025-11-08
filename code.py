import pygame

# кольори
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# налаштування Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

# ваш код
img_player = pygame.image.load("DinoRun1.png").convert_alpha()

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

# клас головного героя

# клас кактуса

# клас групи кактусів

# ігрові об'єкти

clock = pygame.time.Clock()
running = True

while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # оновлення ігрових об'єктів

    # заливка екрана кольором
    screen.fill(WHITE)

    # відрисовка ігрових об'єктів

    # оновлення дисплея
    pygame.display.flip()

    clock.tick(50)

pygame.quit()
