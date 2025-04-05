from pygame import *
from random import randint
from time import time as timer # ⬅️

# нам потрібні такі картинки:
img_back = "galaxy.jpg"  # фон гри
img_hero = "rocket.png"  # герой
img_enemy = "ufo.png"  # ворог
img_bullet = "bullet.png" # куля
img_ast = "asteroid.png" # астероїд ⬅️


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

# шрифти і написи
font.init()
font2 = font.Font(None, 36)
font1 = font.SysFont(None, 80) # написи для перемоги та поразки
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
emoji_font = font.SysFont("Segoe UI Emoji", 40) # ⬅️


score = 0  # збито кораблів
lost = 0  # пропущено кораблів
goal = 10 # стільки кораблів потрібно збити для перемоги
max_lost = 3 # програли, якщо пропустили стільки
rel_time = False  # прапор, що відповідає за перезаряджання ⬅️
num_fire = 0  # змінна для підрахунку пострілів ⬅️
life = 3  # змінна для підрахунку життів ⬅️


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
    def fire(self): # створюємо після класу булєт
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0


# клас спрайта-ворога
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


# клас спрайта-кулі
class Bullet(GameSprite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.y < 0:
            self.kill()



# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
# створюємо ворогів
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
# створюємо групу для куль (далі робимо метод для пострілу в класі плеєр)
bullets = sprite.Group()

# створення групи спрайтів-астероїдів ⬅️⬅️⬅️
asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Asteroid(img_ast, randint(30, win_width - 30), # один рядок
                     -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)



while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
        # подія натискання на пробіл - спрайт стріляє
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                # перевіряємо, скільки пострілів зроблено і чи не відбувається перезаряджання⬅️
                if num_fire < 5 and rel_time == False: # ⬅️
                    num_fire = num_fire + 1# ⬅️
                    fire_sound.play()# ⬅️ додали відступ
                    ship.fire()# ⬅️ додали відступ

                if num_fire >= 5 and rel_time == False:  # якщо гравець зробив 5 пострілів⬅️
                    last_time = timer()  # засікаємо час, коли це сталося⬅️
                    rel_time = True  # ставимо прапор перезарядки⬅️

    if not finish:
        window.blit(background, (0, 0))

        # пишемо текст на екрані
        text = font2.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        ship.update()
        ship.reset()

        monsters.update()
        monsters.draw(window)

        # рухаємо та оновлюємо кулі
        bullets.update()
        bullets.draw(window)

        # рухаємо та оновлюємо астероїди⬅️
        asteroids.update()
        asteroids.draw(window)

        # перезарядка⬅️
        if rel_time == True:
            now_time = timer()  # зчитуємо час

            if now_time - last_time < 3:  # поки не минуло 3 секунди виводимо інформацію про перезарядку
                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0  # обнулюємо лічильник куль
                rel_time = False  # скидаємо прапор перезарядки

        # перевірка зіткнення кулі та монстрів (і монстр, і куля при зіткненні зникають)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # цей цикл повториться стільки разів, скільки монстрів збито
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80),
                            -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # можливий програш: пропустили занадто багато або герой зіткнувся з ворогом ⬅️⬅️
        # if sprite.spritecollide(ship, monsters, False) or lost >= max_lost: ⬅️ було
        if life == 0 or lost >= max_lost:  # ⬅️⬅️
            finish = True  # програли, ставимо тло і більше не керуємо спрайтами.
            window.blit(lose, (200, 200))

        # якщо спрайт торкнувся ворога зменшує життя⬅️⬅️⬅️⬅️
        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
            sprite.spritecollide(ship, monsters, True)
            sprite.spritecollide(ship, asteroids, True)
            life = life - 1

        hearts = emoji_font.render('❤️' * life, True, (255, 100, 100))
        window.blit(hearts, (win_width - 200, win_height - 50))


        # перевірка виграшу: скільки очок набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
    # цикл спрацьовує кожні 0.05 секунд
    time.delay(50)
