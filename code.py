from pygame import *
from random import randint #⬅️

# нам потрібні такі картинки:
img_back = "galaxy.jpg"  # фон гри
img_hero = "rocket.png"  # герой
img_enemy = "ufo.png"  # ворог ⬅️

# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),
                             (win_width, win_height))

finish = False
run = True

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
fire_sound = mixer.Sound('fire.ogg')

score = 0  # збито кораблів⬅️
lost = 0  # пропущено кораблів⬅️

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  # один рядок
                 size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(  # один рядок
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player(GameSprite):

    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        pass


# клас спрайта-ворога⬅️
class Enemy(GameSprite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1



# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))
        ship.update()
        ship.reset()

        display.update()
    # цикл спрацьовує кожні 0.05 секунд
    time.delay(50)
