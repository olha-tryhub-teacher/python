import time
import random
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy import platform
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.metrics import dp

from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.uix.dialog import (MDDialog,
                               MDDialogHeadlineText,
                               MDDialogButtonContainer)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget


class MoveBackground(MDFloatLayout):
    speed = NumericProperty(1)

    def __init__(self, image_source, speed=1, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed

        self.bg1 = FitImage(source=image_source, size_hint=(1, 1), pos=(0, 0))
        self.bg2 = FitImage(source=image_source, size_hint=(1, 1), pos=(0, Window.height))

        self.add_widget(self.bg1)
        self.add_widget(self.bg2)

    def update(self):
        self.bg1.y -= self.speed
        self.bg2.y -= self.speed

        if self.bg1.top <= 0:
            self.bg1.y = self.bg2.top

        if self.bg2.top <= 0:
            self.bg2.y = self.bg1.top


class Bullet(Image):
    def __init__(self, speed, owner, **kwargs):
        super().__init__(**kwargs)
        self.source = "assets/images/bullet.png"
        self.size_hint = (None, None)
        self.size = (dp(10), dp(30))
        self.speed = speed
        self.owner = owner


class BaseShip(Image):
    hp = NumericProperty(100)
    max_hp = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)


class PlayerShip(BaseShip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = dp(5)

        # [ЗМІНА] Змінні для покадрової анімації гравця
        self.anim_delay = 0.1  # Час між кадрами в секундах
        self._lastAnim = 0
        self._currentAnim = 0

        # Список кадрів анімації з папки rocket
        self.images = [
            "assets/images/rocket/rocket1.png",
            "assets/images/rocket/rocket2.png",
            "assets/images/rocket/rocket3.png",
            "assets/images/rocket/rocket4.png",
            "assets/images/rocket/rocket5.png",
            "assets/images/rocket/rocket6.png",
            "assets/images/rocket/rocket7.png",
            "assets/images/rocket/rocket8.png",
        ]

    # [ЗМІНА] Метод покадрової анімації корабля
    def animate(self, dt):
        self._lastAnim += dt
        if self._lastAnim >= self.anim_delay:
            self._lastAnim = 0
            self._currentAnim = (self._currentAnim + 1) % len(self.images)
            self.source = self.images[self._currentAnim]

    def move(self, keys, screen_width):
        if keys["left"] and self.x > 0:
            self.x -= self.speed
        if keys["right"] and self.right < screen_width:
            self.x += self.speed

    def fire(self):
        bullet = Bullet(speed=dp(10), owner="player")
        bullet.center_x = self.center_x
        bullet.y = self.top
        return bullet


class EnemyShip(BaseShip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = dp(3)
        self.last_shot = time.time()
        self.fire_rate = random.uniform(1.5, 3.0)

    def move(self):
        self.y -= self.speed

    def fire(self):
        bullet = Bullet(speed=dp(-8), owner="enemy")
        bullet.center_x = self.center_x
        bullet.top = self.y
        return bullet


class MainScreen(MDScreen):
    pass


class GameOverScreen(MDScreen):
    pass


class GameScreen(MDScreen):
    fps = 60
    timer = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys = {"left": False, "right": False, "fire": False}
        self.bullets = []
        self.game_event = None
        self.enemies = []
        self.dialog_pause = None
        self.spawn_timer = 0
        self.spawn_delay = 2.0
        self.bg_layers = []

    def on_enter(self, *args):
        self.ids.back.clear_widgets()
        self.bg_layers = [
            MoveBackground(image_source="assets/images/stars_far.png", speed=dp(1)),
            MoveBackground(image_source="assets/images/stars_close.png", speed=dp(2.5))
        ]
        for bg in self.bg_layers:
            self.ids.back.add_widget(bg)

        self.ids.ship.hp = self.ids.ship.max_hp
        self.timer = 0

        for enemy in self.enemies:
            self.ids.front.remove_widget(enemy)
        self.enemies.clear()

        for bullet in self.bullets:
            self.ids.front.remove_widget(bullet)
        self.bullets.clear()

        self.ids.ship.center_x = Window.width / 2
        self.keys = {"left": False, "right": False, "fire": False}
        self.spawn_timer = 0

        self.spawn_enemy()
        self.game_event = Clock.schedule_interval(self.update, 1 / self.fps)

    def on_leave(self, *args):
        if self.game_event:
            self.game_event.cancel()

    def spawn_enemy(self):
        enemy = EnemyShip()
        enemy.x = random.randint(0, int(Window.width - dp(80)))
        enemy.y = Window.height
        self.ids.front.add_widget(enemy)
        self.enemies.append(enemy)

    def update(self, dt):
        self.timer += dt
        for bg in self.bg_layers:
            bg.update()

        self.ids.ship.move(self.keys, Window.width)

        # [ЗМІНА] Викликаємо анімацію корабля у кожному кадрі
        self.ids.ship.animate(dt)

        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_delay:
            self.spawn_enemy()
            self.spawn_timer = 0
            self.spawn_delay = random.uniform(1.0, 3.0)

        for enemy in self.enemies[:]:
            enemy.move()

            if time.time() - enemy.last_shot > enemy.fire_rate:
                new_bullet = enemy.fire()
                self.ids.front.add_widget(new_bullet)
                self.bullets.append(new_bullet)
                enemy.last_shot = time.time()

            if enemy.top < 0:
                self.ids.front.remove_widget(enemy)
                self.enemies.remove(enemy)

        for bullet in self.bullets[:]:
            bullet.y += bullet.speed
            if bullet.y > Window.height or bullet.top < 0:
                self.remove_bullet(bullet)

        self.check_collisions()

    def check_collisions(self):
        # [ЗМІНА] Зіткнення з ворогом тепер віднімає HP замість миттєвого програшу
        for enemy in self.enemies[:]:
            if self.ids.ship.collide_widget(enemy):
                self.ids.ship.hp -= 34  # Віднімаємо частину здоров'я
                self.ids.front.remove_widget(enemy)
                self.enemies.remove(enemy)
                if self.ids.ship.hp <= 0:
                    self.game_over()
                    return

        for bullet in self.bullets[:]:
            if bullet.owner == "player":
                for enemy in self.enemies[:]:
                    if bullet.collide_widget(enemy):
                        self.ids.front.remove_widget(enemy)
                        if enemy in self.enemies:
                            self.enemies.remove(enemy)
                        self.remove_bullet(bullet)
                        break

            elif bullet.owner == "enemy":
                if bullet.collide_widget(self.ids.ship):
                    self.ids.ship.hp -= 15
                    self.remove_bullet(bullet)
                    if self.ids.ship.hp <= 0:
                        self.game_over()
                        return

    def remove_bullet(self, bullet):
        if bullet in self.bullets:
            self.ids.front.remove_widget(bullet)
            self.bullets.remove(bullet)

    def game_over(self):
        if self.game_event:
            self.game_event.cancel()
            self.game_event = None
        self.manager.current = "game_over"

    def fire(self):
        new_bullet = self.ids.ship.fire()
        self.ids.front.add_widget(new_bullet)
        self.bullets.append(new_bullet)

    def pause_game(self):
        if self.game_event:
            self.game_event.cancel()
            self.game_event = None

        if not self.dialog_pause:
            self.dialog_pause = MDDialog(
                MDDialogHeadlineText(text="PAUSE"),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="RESUME"),
                        on_release=self.resume_game
                    )
                ),
            )
        self.dialog_pause.open()

    def resume_game(self, *args):
        self.dialog_pause.dismiss()
        self.game_event = Clock.schedule_interval(self.update, 1 / self.fps)


class ShooterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"

        self.sm = MDScreenManager()
        self.sm.add_widget(MainScreen(name="main"))
        self.sm.add_widget(GameScreen(name="game"))
        self.sm.add_widget(GameOverScreen(name="game_over"))

        return self.sm


if platform != "android":
    Window.size = (450, 800)
    Window.top = 100
    Window.left = 600

app = ShooterApp()
app.run()