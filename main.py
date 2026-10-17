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
