import pygame as pg

# кольори
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 500
HEIGHT = 500

# налаштування Pygame
pg.init()
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()


class Button():
    def __init__(self, x, y, text, w):
        self.rect = pg.Rect(x, y, w, 50)
        self.rect_image = pg.Surface((w, 50))
        self.rect_image.fill(BLUE)
        self.rect_image_active = pg.Surface((w, 50))
        self.rect_image_active.fill(GREEN)

        self.font = pg.font.Font(None, 32)
        self.text_image = self.font.render(text, True, WHITE)
        self.text_rect = pg.Rect(x, y, len(text) * 20, 32)
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.top = y + 5
        self.active = False
        self.fn = None
        self.activated = False

    def update(self):
        x, y = pg.mouse.get_pos()
        collision = self.rect.collidepoint(x, y)
        click = pg.mouse.get_pressed()[0]

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


# завантаження картинок
image_ball = pg.image.load("Ball.png").convert_alpha()
image_block1 = pg.image.load("Block1.png").convert_alpha()
image_block2 = pg.image.load("Block2.png").convert_alpha()
image_block3 = pg.image.load("Block3.png").convert_alpha()
image_platform1 = pg.image.load("Platform1.png").convert_alpha()
image_bg = pg.image.load("background.png").convert()


class TextLabel:
    def __init__(self, x, y, size=32, color=BLACK):
        self.x = x
        self.y = y
        self.color = color
        self.image = None
        self.font = pg.font.Font(None, size)

    def set_text(self, text):
        self.image = self.font.render(text, True, self.color)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Sprite:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = pg.Rect(x, y, self.image.get_width(), self.image.get_height())

    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.left, self.rect.top))


class Player(Sprite):
    def __init__(self, x, y, image_base):
        super().__init__(x, y, image_base)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.left -= 8
        if keys[pg.K_RIGHT]:
            self.rect.left += 8


class Ball(Sprite):
    def __init__(self, x, y, image, velocity):
        super().__init__(x, y, image)
        self.SPEED = velocity
        self.velocityx = velocity
        self.velocityy = -velocity

    def update(self):
        self.rect.left += self.velocityx
        self.rect.top += self.velocityy

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocityx = -self.velocityx
        if self.rect.top < 0:
            self.velocityy = self.SPEED

    def change_velocity(self, player):
        self.velocityy = -self.SPEED
        # горизонтальна швидкість не змінюється


# створення об'єктів гри
ball = Ball(100, HEIGHT // 2, image_ball, 4)
player = Player(WIDTH // 2 - 50, HEIGHT - 60, image_platform1)

score = 0
label = TextLabel(370, 470, 28)
label.set_text(f"Score: {score}")

label_win = TextLabel(100, 250, 50, GREEN)  # ⬅️
label_win.set_text(f"WIN!!!")  # ⬅️

label_lose = TextLabel(100, 250, 50, RED)  # ⬅️
label_lose.set_text(f"LOSE!!!")  # ⬅️

blocks = []


# --- перехід в різні частини гри  ---
def go_to_game():
    global game_part
    game_part = "game"
    for i in range(15):
        row = i // 5
        col = i % 5
        blocks.append(Sprite(50 + col * 80, 20 + row * 40,
                             [image_block1, image_block2, image_block3][row]))
    ball.rect.x = 100
    ball.rect.y = HEIGHT // 2
    player.rect.x = WIDTH // 2 - 50
    player.rect.y = HEIGHT - 60

def go_to_gameover():
    global game_part
    game_part = "gameover"



def go_to_victory():
    global game_part
    game_part = "victory"


def go_to_menu():
    global game_part
    game_part = "menu"


# ------------------ гра ------------------
def update_game():
    global score
    ball.update()
    player.update()

    # перевірка програшу
    if ball.rect.top > HEIGHT:
        go_to_gameover()

    if len(blocks) == 0:  # ⬅️
        go_to_victory()

    if player.collide(ball):
        ball.change_velocity(player)

    screen.blit(image_bg, (0, 0))

    for b in blocks[:]:
        if b.collide(ball):
            blocks.remove(b)
            ball.velocityy = ball.SPEED
            score += 100
            label.set_text(f"Score: {score}")
        b.draw(screen)

    ball.draw(screen)
    label.draw(screen)
    player.draw(screen)





# Кнопки меню
start_button = Button(100, 200, "Почати гру", 300)
start_button.onclick(go_to_game)

# Кнопки для екранів результату
back_menu_button = Button(100, 200, "Назад у меню", 300)
back_menu_button.onclick(go_to_menu)


# --- головний цикл ---
game_part = "menu"
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
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
        update_game()


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
    pg.display.flip()
    clock.tick(50)

pg.quit()
