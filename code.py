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
img_cactus=pygame.image.load("SmallCactus1.png")
img_cloud=pygame.image.load("Cloud.png")
img_ground=pygame.image.load("Trak.png")
class Object:
    def __init__(self, x, y, img):
        self.img=img
        self.rect=pygame.Rect(x, y, self.img.get_width(),self.img.get_htight())
    def draw(self,screen):
        screen.bilt(self.img,(self.rect.left, self.rect.top))
# клас гравця з керуванням
class Player(Object):
    def __init__(self, x, y):
        super().__init__(x, y, img_player)
        self.max_y = y
        self.velocity = 0
        self.GRAVITY = 0.007
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
