# підключення pygame
import pygame

# кольори
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 50

# налаштування Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
###############################
#ваш код
p = pygame.Surface((100, 100))
p.fill(WHITE)
rect = pygame.Rect((100, 100), (200, 200))

# створення годинника
clock = pygame.time.Clock()

running = True


while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rect.x -= 5
            if event.key == pygame.K_d:
                rect.x += 5
            if event.key == pygame.K_w:
                rect.y -= 5
            if event.key == pygame.K_s:
                rect.y += 5

    # заливка екрана кольором, відображення прямокутників
    screen.fill(BLUE)
    x = rect.x
    y = rect.y
    screen.blit(p, (x, y))
    
    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
