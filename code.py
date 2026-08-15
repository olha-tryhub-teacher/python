from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

# Розмір вікна (для ПК, на Android не впливає)
Window.size = (450, 900)


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Основний контейнер
        layout = BoxLayout(orientation="vertical",
                           padding="20dp", spacing="20dp")

        # Картинка у верхній частині меню
        img_title = Image(source="img.png", size_hint=(1, 0.5))
        layout.add_widget(img_title)

        # Текстовий заголовок
        lbl_title = Label(text="Main Menu", font_size="40sp",
                          size_hint=(1, 0.2))
        layout.add_widget(lbl_title)

        # Кнопка Play
        btn_play = Button(text="PLAY", size_hint=(1, 0.15),
                          font_size="20sp")
        btn_play.bind(on_press=self.go_game)
        layout.add_widget(btn_play)

        # Кнопка Settings
        btn_settings = Button(text="SETTINGS", size_hint=(1, 0.15),
                              font_size="20sp")
        btn_settings.bind(on_press=self.go_settings)
        layout.add_widget(btn_settings)

        # Кнопка Exit
        btn_exit = Button(text="EXIT", size_hint=(1, 0.15),
                          font_size="20sp")
        btn_exit.bind(on_press=self.exit_app)
        layout.add_widget(btn_exit)

        self.add_widget(layout)

    # Перехід до екрана гри
    def go_game(self, *args):
        self.manager.current = "game"

    # Перехід до екрана налаштувань
    def go_settings(self, *args):
        self.manager.current = "settings"

    # Вихід з програми
    def exit_app(self, *args):
        app.stop()


class Game(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Основний контейнер
        layout = BoxLayout(orientation="vertical", padding="20dp", spacing="20dp")

        # Надпис "Game Screen"
        lbl_game = Label(text="Game Screen", font_size="40sp")
        layout.add_widget(lbl_game)

        # Кнопка повернення
        btn_back = Button(text="Back to Menu", size_hint=(1, 0.2), font_size="20sp")
        btn_back.bind(on_press=self.go_menu)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    # Повернення до меню
    def go_menu(self, *args):
        self.manager.current = "menu"


class Settings(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Основний контейнер
        layout = BoxLayout(orientation="vertical", padding="20dp", spacing="20dp")

        # Заголовок
        lbl_settings = Label(text="Settings", font_size="40sp")
        layout.add_widget(lbl_settings)

        # Кнопка повернення
        btn_back = Button(text="Back to Menu", size_hint=(1, 0.2), font_size="20sp")
        btn_back.bind(on_press=self.go_menu)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    # Повернення до меню
    def go_menu(self, *args):
        self.manager.current = "menu"


class MediumApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Game(name="game"))
        sm.add_widget(Settings(name="settings"))
        return sm


app = MediumApp()
app.run()
