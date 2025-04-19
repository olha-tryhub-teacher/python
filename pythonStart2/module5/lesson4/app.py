from pygame import *

# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# нові класи-спадкоємці
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# клас-спадкоємець для спрайта-ворога (переміщається сам)
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


# клас для спрайтів-перешкод ⬇️⬇️⬇️
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3,
                 wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# Ігрова сцена:
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"),
                             (win_width, win_height))

# Змінити класи для персонажів гри:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

# стіни ⬇️⬇️⬇️
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)

# написи ⬇️⬇️⬇️
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


game = True
clock = time.Clock()
FPS = 60

# new value for end game
finish = False


# музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

# звуки ⬇️⬇️⬇️
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))

        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()
        # відмалювати стіни ⬇️⬇️⬇️
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

    # Ситуація "Програш" ⬇️⬇️⬇️
    if (sprite.collide_rect(player, monster)
            or sprite.collide_rect(player, w1)
            or sprite.collide_rect(player, w2)
            or sprite.collide_rect(player, w3)):
        window.blit(lose, (200, 200))
        if not finish:
            kick.play()
            finish = True

    # Ситуація "Перемога" ⬇️⬇️⬇️
    if sprite.collide_rect(player, final):
        window.blit(win, (200, 200))
        if not finish:
            money.play()
            finish = True

    display.update()
    clock.tick(FPS)
