    # ДОДАНО: звуки завантажуються один раз після запуску застосунку.
    def on_start(self):
        self.button_sound = SoundLoader.load("assets/sounds/vgmenuhighlight.ogg")
        self.fish_sound = SoundLoader.load("assets/sounds/pop1.ogg")
        self.music_sound = None
        self.play_music("assets/sounds/Whimsy Walking.wav")  # ДОДАНО: запускаємо перший трек зі списку нижче.

    # ДОДАНО: змінює кольорову тему без перезапуску застосунку.
    def set_theme(self, theme):
        self.theme = theme

    # ДОДАНО: відтворює короткий звук натискання кнопки.
    def play_button_sound(self):
        if self.button_sound:
            self.button_sound.stop()
            self.button_sound.play()

    # ДОДАНО: відтворює короткий звук влучання по рибі.
    def play_fish_sound(self):
        if self.fish_sound:
            self.fish_sound.stop()
            self.fish_sound.play()

    # ДОДАНО: зупиняє попередній трек та запускає вибраний фоновий трек.
    def play_music(self, track_name):
        if self.music_sound:
            self.music_sound.stop()

        # ДОДАНО: точні назви двох фонових треків у папці assets/sounds.
        self.music_sound = SoundLoader.load("assets/sounds/Whimsy Walking.wav")
        if self.music_sound:
            self.music_sound.loop = True
            self.music_sound.volume = 0.4
            self.music_sound.play()
