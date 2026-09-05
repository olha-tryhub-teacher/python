# Спільний стиль кнопок меню
<ButtonMenu@Button>:
    font_size: "20sp"
    size_hint: 1, 0.15
    background_normal: ''
    # ДОДАНО: кольори кнопки залежать від вибраної теми.
    background_color: from_hex(light_button) if app.theme == "light" else from_hex(dark_button)
    color: from_hex(light_text) if app.theme == "light" else from_hex(dark_text)
    on_press:
        # ДОДАНО: колір кнопки під час натискання для обох тем.
        self.background_color = from_hex(light_button_pressed) if app.theme == "light" else from_hex(dark_button_pressed)
    on_release:
        # ДОДАНО: повернення кольору й звук після натискання кнопки.
        self.background_color = from_hex(light_button) if app.theme == "light" else from_hex(dark_button)
        app.play_button_sound()
