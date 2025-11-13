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
clock = pygame.time.Clock()


class Button():
    def __init__(self, x, y, text, w):
        self.rect = pygame.Rect(x, y, w, 50)
        self.rect_image = pygame.Surface((w, 50))
        self.rect_image.fill(BLUE)
        self.rect_image_active = pygame.Surface((w, 50))
        self.rect_image_active.fill(GREEN)

        self.font = pygame.font.Font(None, 32)
        self.text_image = self.font.render(text, True, WHITE)
        self.text_rect = pygame.Rect(x, y, len(text) * 20, 32)
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.top = y + 5
        self.active = False
        self.fn = None
        self.activated = False

    def update(self):
        x, y = pygame.mouse.get_pos()
        collision = self.rect.collidepoint(x, y)
        click = pygame.mouse.get_pressed()[0]

        if not click and self.activated:
            self.activated = False

        if collision:
            self.active = True
            if click and self.fn and not self.activated:
                self.activated = True
                self.fn()
        else:
            self.active = False

    def draw(self, surface):
        if self.active:
            surface.blit(self.rect_image, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.rect_image_active, (self.rect.x, self.rect.y))
        surface.blit(self.text_image, (self.text_rect.x, self.text_rect.y))

    def onclick(self, fn):
        self.fn = fn


# --- створення кнопок ДО циклу ---
def go_to_game():
    global game_part
    game_part = "game"


def go_to_gameover():
    global game_part
    game_part = "gameover"


def go_to_victory():
    global game_part
    game_part = "victory"


def go_to_menu():
    global game_part
    game_part = "menu"


# Кнопки меню
start_button = Button(100, 200, "Почати гру", 300)
start_button.onclick(go_to_game)

# Кнопки гри
gameover_button = Button(100, 100, "Програш", 300)
victory_button = Button(100, 300, "Виграш", 300)
gameover_button.onclick(go_to_gameover)
victory_button.onclick(go_to_victory)

# Кнопки для екранів результату
back_menu_button = Button(100, 200, "Назад у меню", 300)
back_menu_button.onclick(go_to_menu)

# --- головний цикл ---
game_part = "menu"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очищення екрану
    screen.fill(WHITE)

    # Вибір кнопок за поточним станом
    if game_part == "menu":
        # Оновлення і малювання кнопок
        start_button.update()
        start_button.draw(screen)
    elif game_part == "game":
        # Оновлення і малювання кнопок
        gameover_button.update()
        gameover_button.draw(screen)
        victory_button.update()
        victory_button.draw(screen)
    elif game_part == "victory":
        # Оновлення і малювання кнопок
        start_button.update()
        start_button.draw(screen)
    elif game_part == "gameover":
        # Оновлення і малювання кнопок
        back_menu_button.update()
        back_menu_button.draw(screen)

    # Оновлення екрану
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
