    # КЛІК ПО РИБІ
    def on_touch_down(self, touch):
        # Якщо клік був не по рибі або вона прозора — передаємо клік далі
        if not self.collide_point(*touch.pos) or not self.opacity:
            return super().on_touch_down(touch)

        self.hp_current -= 1
        self.GAME_SCREEN.score += 1

        if self.hp_current <= 0:
            self.defeated()
            Clock.schedule_once(self.GAME_SCREEN.level_complete, 1.2)
        else:
            self.stop_timers()
            self.hide_fish()

        # Повертаємо True, щоб система знала: "Клік був влучним, ми його обробили!"
        return True
