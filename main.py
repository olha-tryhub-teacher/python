from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy import platform
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.uix.image import Image

# [ЗМІНА] Імпортуємо компоненти для діалогового вікна паузи (KivyMD)
import time
import random
from kivy.metrics import dp
from kivymd.uix.dialog import (MDDialog,
                               MDDialogHeadlineText,
                               MDDialogButtonContainer)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget


# [ЗМІНА] Куля тепер приймає параметр speed, щоб визначати напрямок (вгору або вниз)
class Bullet(Image):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.source = "assets/images/bullet.png"
        self.size_hint = (None, None)
        self.size = (dp(10), dp(30))
        self.speed = speed


# [ЗМІНА] Базовий клас для ВСІХ кораблів (спільна основа)
class BaseShip(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)


# [ЗМІНА] Клас корабля гравця, який наслідує BaseShip
class PlayerShip(BaseShip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = dp(5)

    # [ЗМІНА] Логіка керування винесена безпосередньо в клас корабля
    def move(self, keys, screen_width):
        if keys["left"] and self.x > 0:
            self.x -= self.speed
        if keys["right"] and self.right < screen_width:
            self.x += self.speed

    # [ЗМІНА] Новий метод стрільби всередині гравця
    def fire(self):
        bullet = Bullet(speed=dp(10))
        bullet.center_x = self.center_x
        bullet.y = self.top
        return bullet

# [ЗМІНА] Клас ворожого корабля
class EnemyShip(BaseShip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = dp(3)
        self.last_shot = time.time()
        self.fire_rate = random.uniform(1.5, 3.0)  # Стріляє кожні 1.5 - 3 секунди

    # [ЗМІНА] Метод руху ворога (завжди вниз)
    def move(self):
        self.y -= self.speed

    # Новий метод стрільби всередині ворога
    def fire(self):
        bullet = Bullet(speed=dp(-8))
        bullet.center_x = self.center_x
        bullet.top = self.y
        return bullet


class MainScreen(MDScreen):
    pass


class GameScreen(MDScreen):
    fps = 60
    # ship_speed = 5
    # bullet_speed = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys = {"left": False, "right": False, "fire": False}
        self.bullets = []
        self.game_event = None
        # [ЗМІНА] Додано список ворогів і змінну для меню паузи
        self.enemies = []  # 🆕🆕🆕
        self.dialog_pause = None  # 🆕🆕🆕
        # [ЗМІНА] Змінні для постійного спавну ворогів
        self.spawn_timer = 0
        self.spawn_delay = 2.0  # Час у секундах до появи наступного ворога

    def on_enter(self, *args):
        # [ЗМІНА] При вході створюємо одного ворога зверху
        self.spawn_enemy()  # 🆕🆕🆕
        self.game_event = Clock.schedule_interval(self.update, 1 / self.fps)

    def on_leave(self, *args):
        if self.game_event:
            self.game_event.cancel()

    # [ЗМІНА] Метод створення ворожого корабля у випадковій позиції
    def spawn_enemy(self):
        enemy = EnemyShip()
        enemy.x = random.randint(0, int(Window.width - dp(80)))  # dp(80) - ширина ворога
        enemy.y = Window.height
        self.ids.front.add_widget(enemy)
        self.enemies.append(enemy)

    def update(self, dt):
        # ship = self.ids.ship
        # if self.keys["left"] and ship.x > 0:
        #     ship.x -= self.ship_speed
        # if self.keys["right"] and ship.right < Window.width:
        #     ship.x += self.ship_speed

        # [ЗМІНА] Оновлення стану головного корабля через його власний метод
        self.ids.ship.move(self.keys, Window.width)

        # [ЗМІНА] Таймер спавну ворогів
        self.spawn_timer += dt  # Додаємо час, що пройшов з минулого кадру
        if self.spawn_timer > self.spawn_delay:
            self.spawn_enemy()  # Створюємо ворога
            self.spawn_timer = 0  # Скидаємо таймер на нуль
            self.spawn_delay = random.uniform(1.0, 3.0)  # Робимо наступний спавн випадковим (від 1 до 3 сек)

        # [ЗМІНА] Оновлення ворогів
        for enemy in self.enemies[:]:
            enemy.move()

            # Викликаємо метод стрільби ворожого корабля
            if time.time() - enemy.last_shot > enemy.fire_rate:
                # Отримуємо кулю від ворога
                new_bullet = enemy.fire()
                self.ids.front.add_widget(new_bullet)
                self.bullets.append(new_bullet)

                enemy.last_shot = time.time()

            if enemy.top < 0:
                self.ids.front.remove_widget(enemy)
                self.enemies.remove(enemy)

        # Використовуємо self.bullets[:], щоб можна було безпечно видаляти елементи зі списку
        for bullet in self.bullets[:]:
            # [ЗМІНА] Оновлення позицій куль (вгору або вниз залежить від їхньої швидкості)
            # bullet.y += self.bullet_speed
            bullet.y += bullet.speed
            # Якщо куля вилетіла за межі екрана, видаляємо її зі сцени та списку
            if bullet.y > Window.height:
                self.ids.front.remove_widget(bullet)
                self.bullets.remove(bullet)

    # [ЗМІНА] Метод-міст для кнопки на екрані
    def fire(self):
        # Отримуємо кулю від корабля гравця
        new_bullet = self.ids.ship.fire()
        self.ids.front.add_widget(new_bullet)
        self.bullets.append(new_bullet)

    # [ЗМІНА] Метод для відкриття діалогового вікна паузи
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

    # [ЗМІНА] Метод для відновлення гри після паузи
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

        return self.sm


if platform != "android":
    Window.size = (450, 900)
    Window.top = 100
    Window.left = 600

app = ShooterApp()
app.run()
