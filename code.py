class WaveManager:
    def __init__(self):
        self.wave_number = 1
        self.zombies_per_wave = 5
        self.zombies_remaining = self.zombies_per_wave

    def next_wave(self):
        self.wave_number += 1
        self.zombies_per_wave = 5 + self.wave_number * 2  # щораз більше зомбі
        self.zombies_remaining = self.zombies_per_wave
        self.spawn_wave()

    def spawn_wave(self):
        for _ in range(self.zombies_per_wave):
            zombi = Enemy(img_zombi, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            zombis.add(zombi)

    def zombie_killed(self):
        self.zombies_remaining -= 1
        if self.zombies_remaining <= 0:
            return True  # Хвиля завершена
        return False



Ініціалізуй менеджер хвиль:
wave_manager = WaveManager()
wave_manager.spawn_wave()


Онови частину, де збиваються зомбі:
collides = sprite.groupcollide(zombis, bullets, True, True)
for c in collides:
    score += 1
    if wave_manager.zombie_killed():
        wave_manager.next_wave()  # Запускаємо нову хвилю


💡 Можеш додати текст хвилі на екран:
python
Копіювати
Редагувати
wave_text = font2.render(f'Wave {wave_manager.wave_number}', True, (255, 255, 0))
window.blit(wave_text, (10, 10))


