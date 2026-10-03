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
