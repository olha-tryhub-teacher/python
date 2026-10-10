    def on_enter(self, *args):
        # [ЗМІНА] Очищення сцени від старих куль та ворогів перед новою грою
        for enemy in self.enemies:
            self.ids.front.remove_widget(enemy)
        self.enemies.clear()

        for bullet in self.bullets:
            self.ids.front.remove_widget(bullet)
        self.bullets.clear()

        self.ids.ship.center_x = Window.width / 2
        self.keys = {"left": False, "right": False, "fire": False}
        self.spawn_timer = 0

        # це вже було
        self.spawn_enemy()
        self.game_event = Clock.schedule_interval(self.update, 1 / self.fps)
