import pygame
from random import randint

# Налаштування Pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Кольори та константи
WHITE = (255, 255, 255)
FPS = 50
SPEED = 5


# --- КЛАС ДИНОЗАВРА ---
class Dino:
    def __init__(self):
        self.x = 100
        self.y = 380
        self.max_y = 380
        self.velocity = 0
        self.gravity = 0.7
        self.is_jumping = False

        # Анімація
        self.run_images = [
            pygame.image.load("DinoRun1.png"),
            pygame.image.load("DinoRun2.png")
        ]
        self.jump_image = pygame.image.load("DinoJump.png")
        self.current_img = self.run_images[0]

        self.frame = 0
        self.anim_timer = 0

    def jump(self):
        if not self.is_jumping:
            self.velocity = 15
            self.is_jumping = True

    def update(self):
        # Фізика
        if self.is_jumping:
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.y >= self.max_y:
                self.y = self.max_y
                self.is_jumping = False

        # Анімація
        if self.is_jumping:
            self.current_img = self.jump_image
        else:
            self.anim_timer += 1
            if self.anim_timer >= 5:
                self.frame = (self.frame + 1) % 2
                self.anim_timer = 0
            self.current_img = self.run_images[self.frame]

    def draw(self, screen):
        screen.blit(self.current_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.current_img.get_width(), self.current_img.get_height())


# --- КЛАС КАКТУСА ---
class Cactus:
    def __init__(self):
        self.image = pygame.image.load("SmallCactus1.png")
        self.x = randint(600, 1000)
        self.y = 400

    def update(self):
        # Рух вліво
        self.x -= SPEED
        # Якщо вийшов за лівий край екрану - повертаємо праворуч
        if self.x + self.image.get_width() < 0:
            self.x = randint(600, 1000)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        # Прямокутник для колізій
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


# --- ІНШІ ОБ'ЄКТИ ТА ФОН (Залишаємо простими) ---
img_cloud = pygame.image.load("Cloud.png")
img_ground = pygame.image.load("Track.png")

cloud_x, cloud_y = randint(500, 1000), randint(80, 200)
ground_x, ground_y = 0, 460

# --- СТВОРЕННЯ ГРАВЦЯ ТА ПЕРЕШКОДИ ---
player = Dino()
cactus = Cactus()

running = True

# --- ГОЛОВНИЙ ІГРОВИЙ ЦИКЛ ---
while running:
    # 1. Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Керування
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.jump()

    # 3. Оновлення логіки (Тепер дуже просто!)
    player.update()
    cactus.update()

    # Рух фону (хмари та земля)
    cloud_x -= SPEED
    if cloud_x + img_cloud.get_width() < 0:
        cloud_x, cloud_y = randint(500, 1000), randint(50, 300)

    ground_x -= SPEED
    if ground_x + img_ground.get_width() <= WIDTH:
        ground_x = 0

    # 4. Перевірка колізій
    if player.get_rect().colliderect(cactus.get_rect()):
        print("Game Over! Динозавр врізався в кактус.")
        running = False

        # 5. Малювання
    screen.fill(WHITE)

    # Спочатку малюємо фон
    screen.blit(img_ground, (ground_x, ground_y))
    screen.blit(img_cloud, (cloud_x, cloud_y))

    # Потім об'єкти
    cactus.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
