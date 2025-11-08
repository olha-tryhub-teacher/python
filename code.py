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


# ігрові об'єкти та ігровий цикл
player = Player(100, 380)
enviroment = Enviroment(0, 460)

# створення годинника
clock = pygame.time.Clock()
running = True

while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # заливка екрана кольором, відображення прямокутників
    screen.fill(WHITE)
    player.update()

    enviroment.update()
    enviroment.draw(screen)

    player.draw(screen)

    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
