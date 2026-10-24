from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy import platform
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.uix.image import Image

import time
import random
from kivy.metrics import dp
from kivymd.uix.dialog import (MDDialog,
                               MDDialogHeadlineText,
                               MDDialogButtonContainer)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget

# [ЗМІНА] Додано NumericProperty для автоматичної прив'язки значень (HP, таймер)
from kivy.properties import NumericProperty
# [ЗМІНА] Додано FitImage та MDFloatLayout для створення паралакс-фону
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout


# [ЗМІНА] Клас рухомого фону для паралакс-ефекту з двома зображеннями підряд
class MoveBackground(MDFloatLayout):
    speed = NumericProperty(1)

    def __init__(self, image_source, speed=1, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed

        # Два зображення, одне над іншим для безперервної прокрутки
        self.bg1 = FitImage(source=image_source, size_hint=(1, 1), pos=(0, 0))
        self.bg2 = FitImage(source=image_source, size_hint=(1, 1), pos=(0, Window.height))

        self.add_widget(self.bg1)
        self.add_widget(self.bg2)

    # Метод зміщення фону вниз
    def update(self):
        self.bg1.y -= self.speed
        self.bg2.y -= self.speed

        # Якщо перше зображення повністю вийшло за нижню межу, переносимо його нагору
        if self.bg1.top <= 0:
            self.bg1.y = self.bg2.top

        # Якщо друге зображення повністю вийшло за нижню межу, переносимо його нагору
        if self.bg2.top <= 0:
            self.bg2.y = self.bg1.top


class Bullet(Image):
    def __init__(self, speed, owner, **kwargs):
        super().__init__(**kwargs)
        self.source = "assets/images/bullet.png"
        self.size_hint = (None, None)
        self.size = (dp(10), dp(30))
        self.speed = speed
        self.owner = owner  # Зберігаємо власника


class BaseShip(Image):
    # [ЗМІНА] Додано властивості hp та max_hp через NumericProperty
    hp = NumericProperty(100)
    max_hp = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)


class PlayerShip(BaseShip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = dp(5)

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
        self.fire_rate = random.uniform(1.5, 3.0)  # Стріляє кожні 1.5 - 3 секунди

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
    # [ЗМІНА] Властивість таймера для відображення в KV
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
        # [ЗМІНА] Список об'єктів фону для паралакс-ефекту
        self.bg_layers = []

    def on_enter(self, *args):
        # [ЗМІНА] Ініціалізація або очищення паралакс-фонів
        self.ids.back.clear_widgets()
        self.bg_layers = [
            # Шар з повільною швидкістю (далекий космос)
            MoveBackground(image_source="assets/images/stars_far.png", speed=dp(1)),
            # Шар із більшою швидкістю (ближчі об'єкти)
            MoveBackground(image_source="assets/images/stars_close.png", speed=dp(2.5))
        ]
        for bg in self.bg_layers:
            self.ids.back.add_widget(bg)

        # [ЗМІНА] Скидання HP гравця та таймера
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
        enemy.x = random.randint(0, int(Window.width - dp(80)))  # dp(80) - ширина ворога
        enemy.y = Window.height
        self.ids.front.add_widget(enemy)
        self.enemies.append(enemy)

    def update(self, dt):
        # [ЗМІНА] Оновлення часу та шарів паралакс-фону
        self.timer += dt
        for bg in self.bg_layers:
            bg.update()

        self.ids.ship.move(self.keys, Window.width)

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
        # 1. Перевірка зіткнення корабля гравця з ворогами
        for enemy in self.enemies[:]:
            if self.ids.ship.collide_widget(enemy):
                self.game_over()
                return

        # 2. Перевірка колізій куль
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
                    # [ЗМІНА] Зменшуємо HP гравця при влучанні кулі
                    self.ids.ship.hp -= 15
                    # [ЗМІНА] додаємо умову
                    if self.ids.ship.hp <= 0:
                        self.remove_bullet(bullet)
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
