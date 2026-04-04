import pygame as pg
from random import randint

# --- НАЛАШТУВАННЯ ---
WIDTH, HEIGHT = 1200, 800
GAP_SIZE = 280
PIPE_WIDTH = 140

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 80)

        # Ресурси
        self.bg = pg.transform.scale(pg.image.load('images/background.png'),
                                     (WIDTH, HEIGHT))
        self.bird_img = pg.transform.scale(pg.image.load('images/player.png'),
                                           (90, 70))
        self.pipe_img = pg.image.load('images/pipe.png')

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
                           'bot': pg.Rect(x, h + GAP_SIZE, PIPE_WIDTH, # один рядок ⬇️
                                          HEIGHT - h - GAP_SIZE),
                           'passed': False})

    def draw_pipe(self, rect, flip=False):
        img = pg.transform.scale(self.pipe_img, (rect.width, rect.height))
        if flip: img = pg.transform.flip(img, False, True)
        self.screen.blit(img, (rect.x, rect.y))

    def jump_action(self):
        if not self.lose:
            self.vel = self.jump

    def update(self):
        if not self.lose:
            # Фізика падіння
            self.vel += self.gravity
            self.bird.y += self.vel

            if self.bird.bottom > HEIGHT or self.bird.top < 0:
                self.lose = True

            for p in self.pipes[:]:
                p['top'].x -= 8
                p['bot'].x -= 8
                if self.bird.colliderect(p['top']) or self.bird.colliderect(p['bot']):
                    self.lose = True
                if not p['passed'] and p['top'].right < self.bird.left:
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
            msg = self.font.render("GAME OVER - Press 'R'", True, 'red')
            self.screen.blit(msg, (WIDTH // 2 - 300, HEIGHT // 2))

# --- ЗАПУСК ---
game = Game()
while True:
    game.update()
    game.draw()
    pg.display.update()

    for e in pg.event.get():
        if e.type == pg.QUIT: 
            exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE: # Стрибок на пробіл
                game.jump_action()
            if e.key == pg.K_r and game.lose: # Перезапуск
                game.reset()

    game.clock.tick(60)
