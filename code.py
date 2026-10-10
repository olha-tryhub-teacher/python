    # [ЗМІНА] Окремий метод для перевірки всіх зіткнень
    def check_collisions(self):
        # 1. Перевірка зіткнення корабля гравця з ворогами
        for enemy in self.enemies[:]:
            # collide_widget перевіряє, чи накладаються координати двох віджетів
            if self.ids.ship.collide_widget(enemy):
                self.game_over()
                return  # Якщо гра завершена, далі не перевіряємо

        # 2. Перевірка колізій куль
        for bullet in self.bullets[:]:
            # Якщо це куля гравця
            if bullet.owner == "player":
                for enemy in self.enemies[:]:
                    if bullet.collide_widget(enemy):
                        # Куля потрапила у ворога: видаляємо ворога та кулю
                        self.ids.front.remove_widget(enemy)
                        if enemy in self.enemies:
                            self.enemies.remove(enemy)
                        self.remove_bullet(bullet)
                        break  # Кулю знищено, виходимо з внутрішнього циклу

            # Якщо це куля ворога
            elif bullet.owner == "enemy":
                if bullet.collide_widget(self.ids.ship):
                    # Куля потрапила в гравця: гра завершується
                    self.remove_bullet(bullet)
                    self.game_over()
                    return

    # [ЗМІНА] Окремий метод для безпечного видалення кулі
    def remove_bullet(self, bullet):
        if bullet in self.bullets:
            self.ids.front.remove_widget(bullet)
            self.bullets.remove(bullet)

    # [ЗМІНА] Окремий метод для логіки програшу
    def game_over(self):
        # Зупиняємо таймер гри
        if self.game_event:
            self.game_event.cancel()
            self.game_event = None
        # Перекидаємо на екран програшу
        self.manager.current = "game_over"
