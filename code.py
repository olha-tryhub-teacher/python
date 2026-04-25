import pygame
from settings import *
from ui import Button

def main():
    # Ініціалізація
    pygame.init()
    pygame.display.set_caption("Фортепіано")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Створення клавіш (кнопок)
    keys = []
    key_width = WIDTH // 8

    for i in range(7):
        # Розраховуємо позицію кожної клавіші
        x_pos = i * key_width + 45
        # Беремо звук зі списку (якщо звуків менше ніж 8, використовуємо остачу від ділення)
        sound_path = SOUND_FILES[i]

        btn = Button(
            x=x_pos, y=100, width=key_width - 2, 
            height=250, color=WHITE, sound_path=sound_path)
        keys.append(btn)
