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
