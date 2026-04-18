import pygame as pg
from random import randint
import sounddevice as sd  # 1. Імпорт бібліотеки для захоплення звуку з мікрофона
import numpy as np        # 2. Імпорт для математичних розрахунків (рівень гучності)

# --- НАЛАШТУВАННЯ ---
WIDTH, HEIGHT = 1200, 800
GAP_SIZE = 280
PIPE_WIDTH = 140
THRESH = 0.03  # 3. Поріг чутливості: якщо звук гучніший за це число, пташка летить вгору

# --- АУДІО МІКРОФОН ---
mic_level = 0  # 4. Глобальна змінна, де зберігається поточна гучність


def audio_cb(indata, frames, time, status):
    """ 5. Функція-колбек, яка постійно отримує дані з мікрофона в реальному часі """
    global mic_level
    # Рахуємо середньоквадратичне значення (RMS) — це і є фізична гучність звуку
    rms = np.sqrt(np.mean(indata ** 2))
    # Згладжуємо значення, щоб рух пташки не був надто сіпаним
    mic_level = 0.5 * mic_level + 0.35 * rms


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 80)

        # Ресурси
        self.bg = pg.transform.scale(pg.image.load('images/background.png'), (WIDTH, HEIGHT))
        self.bird_img = pg.transform.scale(pg.image.load('images/player.png'), (90, 70))
        self.pipe_img = pg.image.load('images/pipe.png')

        # todo Завантаження звуків
        self.snd_flap = pg.mixer.Sound('sounds/flap.ogg')
        self.snd_coin = pg.mixer.Sound('sounds/coin.ogg')
        self.snd_collision = pg.mixer.Sound('sounds/collision.ogg')

        self.reset()

    def reset(self):
        self.bird = pg.Rect(150, HEIGHT // 2, 90, 70)
        self.pipes = []
        self.score = 0
        self.lose = False
        self.vel = 0
        self.gravity = 0.7
        self.jump = -10
        self.spawn_pipe(WIDTH)

    def spawn_pipe(self, x):
        h = randint(100, HEIGHT - GAP_SIZE - 100)
        self.pipes.append({'top': pg.Rect(x, 0, PIPE_WIDTH, h),
                           'bot': pg.Rect(x, h + GAP_SIZE, PIPE_WIDTH, HEIGHT - h - GAP_SIZE),
                           'passed': False})

    def draw_pipe(self, rect, flip=False):
        img = pg.transform.scale(self.pipe_img, (rect.width, rect.height))
        if flip: img = pg.transform.flip(img, False, True)
        self.screen.blit(img, (rect.x, rect.y))

    def update(self):
        if not self.lose:
            # 6. ПЕРЕВІРКА ВХІДНОГО ЗВУКУ:
            # Якщо поточний рівень гучності вище порогу — робимо стрибок
            # self.vel += self.gravity
            # self.bird.y += self.vel
            if mic_level > THRESH:
                if self.vel >= 0:
                    self.snd_flap.play()
                self.vel = self.jump
            else:
                self.vel += self.gravity

            self.bird.y += self.vel

            if self.bird.bottom > HEIGHT or self.bird.top < 0:
                self.snd_collision.play()
                self.lose = True

            for p in self.pipes[:]:
                p['top'].x -= 8
                p['bot'].x -= 8

                if self.bird.colliderect(p['top']) or self.bird.colliderect(p['bot']):
                    self.snd_collision.play()
                    self.lose = True

                if not p['passed'] and p['top'].right < self.bird.left:
                    self.snd_coin.play()
                    self.score += 1
                    p['passed'] = True

            self.pipes = [p for p in self.pipes if p['top'].right > 0]
            if len(self.pipes) < 4: self.spawn_pipe(self.pipes[-1]['top'].x + 600)
        else:
            self.bird.y += 10

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        for p in self.pipes:
            self.draw_pipe(p['top'], True)
            self.draw_pipe(p['bot'])
        self.screen.blit(self.bird_img, self.bird)

        txt = self.font.render(str(self.score), True, 'white')
        self.screen.blit(txt, (WIDTH // 2, 50))

        if self.lose:
            msg = self.font.render("GAME OVER - 'R' or Shout", True, 'red')
            self.screen.blit(msg, (WIDTH // 2 - 300, HEIGHT // 2))


# --- ЗАПУСК ---
game = Game()

# 7. ЗАПУСК ПОТОКУ МІКРОФОНА:
#InputStream відкриває мікрофон і передає дані у функцію audio_cb
with sd.InputStream(callback=audio_cb):
    while True:
        game.update()
        game.draw()
        pg.display.update()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            # if e.key == pg.K_SPACE: # Стрибок на пробіл
            #     game.jump_action()
            if e.type == pg.KEYDOWN and e.key == pg.K_r:
                game.reset()

        # 8. ПЕРЕЗАПУСК ГОЛОСОМ:
        # Якщо ми програли, але знову крикнули (гучність у 4 рази вища за поріг) — гра почнеться заново
        if game.lose and mic_level > THRESH * 4:
            game.reset()

        game.clock.tick(60)
