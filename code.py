import pygame as pg

BLACK = (0, 0, 0)
WIDTH = 500
HEIGHT = 500

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

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
ball = Ball(100, HEIGHT//2, image_ball, 4)
player = Player(WIDTH//2 - 50, HEIGHT - 60, image_platform1)

score = 0
label = TextLabel(370, 470, 28)
label.set_text(f"Score: {score}")

blocks = []
for i in range(15):
    row = i // 5
    col = i % 5
    blocks.append(Sprite(50 + col*80, 20 + row*40,
                  [image_block1, image_block2, image_block3][row]))

clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    ball.update()
    player.update()

    # перевірка програшу
    if ball.rect.top > HEIGHT:
        print("Game Over!")
        running = False

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

    pg.display.flip()
    clock.tick(50)

pg.quit()
