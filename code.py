import pygame
from settings import *
from ui import Button, Slider


def main():
    pygame.init()
    pygame.display.set_caption("Піаніно з регулятором гучності")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Створюємо слайдер (позиція x=45, y=50, ширина 200)
    volume_slider = Slider(45, 50, 200, 20, val=0.5)

    keys = []
    key_width = WIDTH // 8
    for i in range(7):
        btn = Button(
            x=i * key_width + 45,
            y=120,
            width=key_width - 5,
            height=230,
            sound_path=SOUND_FILES[i]
        )
        # Встановлюємо початкову гучність 50%
        btn.sound.set_volume(0.5)
        keys.append(btn)

    while True:
        screen.fill(GRAY)

        # Підпис для слайдера
        font = pygame.font.SysFont(None, 24)
        img = font.render(f"Гучність: {int(volume_slider.val * 100)}%", True, BLACK)
        screen.blit(img, (45, 25))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Якщо слайдер рухається, змінюємо гучність усіх звуків
            if volume_slider.handle_event(event):
                for key in keys:
                    key.sound.set_volume(volume_slider.val)

            for key in keys:
                key.handle_event(event)

        # Малювання
        volume_slider.draw(screen)
        for key in keys:
            key.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

main()
