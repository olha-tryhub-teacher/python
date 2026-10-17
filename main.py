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
