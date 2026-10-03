from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy import platform
from kivy.core.window import Window

# [ЗМІНА] Додаємо імпорт Clock для регулярного оновлення (таймеру)
from kivy.clock import Clock
# [ЗМІНА] Додаємо імпорт Image для створення класу кулі
from kivy.uix.image import Image


# [ЗМІНА] Створюємо окремий клас для кулі, як вимагається у завданні
class Bullet(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Вкажіть шлях до вашої картинки кулі, або залиште так, якщо створите її пізніше
        self.source = "assets/images/bullet.png"
        self.size_hint = (None, None)
        self.size = (10, 30)

class MainScreen(MDScreen):
    pass

class GameScreen(MDScreen):
    # [ЗМІНА] Додані змінні для швидкості гри (кадри, корабель, куля)
    fps = 60
    ship_speed = 5
    bullet_speed = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # [ЗМІНА] Словник подій для запам'ятовування натиснутих кнопок
        self.keys = {"left": False, "right": False, "fire": False}
        # [ЗМІНА] Список для зберігання всіх випущених куль
        self.bullets = []
        self.game_event = None

    def on_enter(self, *args):
        # [ЗМІНА] Налаштування регулярного оновлення. Викликаємо self.update кожний кадр
        self.game_event = Clock.schedule_interval(
            self.update, 1 / self.fps)

    def on_leave(self, *args):
        # [ЗМІНА] Зупиняємо гру, якщо вийшли з екрана
        if self.game_event:
            self.game_event.cancel()

    def update(self, dt):
        # [ЗМІНА] Метод руху корабля. Читаємо словник подій
        ship = self.ids.ship

        # Рух вліво (якщо кнопка натиснута і корабель не виїхав за лівий край)
        if self.keys["left"] and ship.x > 0:
            ship.x -= self.ship_speed

        # Рух вправо (якщо кнопка натиснута і корабель не виїхав за правий край)
        if self.keys["right"] and ship.right < Window.width:
            ship.x += self.ship_speed

        # [ЗМІНА] Оновлення позицій куль у кожному кадрі
        # Використовуємо self.bullets[:], щоб можна було безпечно видаляти елементи зі списку
        for bullet in self.bullets[:]:
            bullet.y += self.bullet_speed
            # Якщо куля вилетіла за межі екрана, видаляємо її зі сцени та списку
            if bullet.y > Window.height:
                self.ids.front.remove_widget(bullet)
                self.bullets.remove(bullet)

    # [ЗМІНА] Створено метод стрільби
    def fire(self):
        # Створюємо нову кулю
        bullet = Bullet()

        # Задаємо їй координати центру нашого корабля
        bullet.center_x = self.ids.ship.center_x
        bullet.y = self.ids.ship.top

        # Додаємо її на шар front і записуємо у наш список
        self.ids.front.add_widget(bullet)
        self.bullets.append(bullet)


class ShooterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # [ЗМІНА] Змінено на Dark для космічної теми
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