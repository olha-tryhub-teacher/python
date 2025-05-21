if timer() - bonus_spawn_time >= 10:
    bonus = BonusShip(img_enemy2, 50, 50, randint(2, 4))  # використовується img_enemy2 або окрема картинка
    bonus_ships.add(bonus)
    bonus_spawn_time = timer()
