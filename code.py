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


class GameSprite:
    def __init__(self, x, y, w, h, color, speed=0):
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed

    def draw(self, surface):
        # Відображення гравця на заданій поверхні (екрані)
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_player(self, keys):
        """Рух гравця за стрілками"""
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def collides(self, other):
        return self.rect.colliderect(other.rect)


# --- створення кнопок  ---
def go_to_game():
    global game_part
    game_part = "game"
    player.rect.x, player.rect.y = 215, 430


def go_to_gameover():
    global game_part
    game_part = "gameover"


def go_to_victory():
    global game_part
    game_part = "victory"


def go_to_menu():
    global game_part
    game_part = "menu"


# ------------------ Міні-гра ------------------
def update_game(keys):
    player.move_player(keys)
    if player.collides(goal):
        go_to_victory()
    elif player.collides(enemy):
        go_to_gameover()



# Кнопки меню
start_button = Button(100, 200, "Почати гру", 300)
start_button.onclick(go_to_game)

# Кнопки для екранів результату
back_menu_button = Button(100, 200, "Назад у меню", 300)
back_menu_button.onclick(go_to_menu)

player = GameSprite(215, 430, 70, 70, BLUE, 5)
goal = GameSprite(430, 0, 70, 70, GREEN)
enemy = GameSprite(0, 0, 70, 70, RED)

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
        keys = pygame.key.get_pressed()
        update_game(keys)
        goal.draw(screen)
        enemy.draw(screen)
        player.draw(screen)

    elif game_part == "victory":
        screen.fill(GREEN)
        # Оновлення і малювання кнопок
        back_menu_button.update()
        back_menu_button.draw(screen)
    elif game_part == "gameover":
        screen.fill(RED)
        # Оновлення і малювання кнопок
        back_menu_button.update()
        back_menu_button.draw(screen)

    # Оновлення екрану
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
