# --- Створення об'єктів гри ---
enemy1 = Enemy(200, 100, "red", "square", 30)
enemy2 = Enemy(-200, -100, "red", "square", 30)
player = Player(0, -180, "navy", "turtle", 10)
finish = Sprite(0, 180, "gold", "triangle")


# --- Основна ігрова функція (цикл) ---
def game():
    # Рух ворогів
    enemy1.move()
    enemy2.move()


    # Перевірка програшу
    if player.touch_t(enemy1) or player.touch_t(enemy2):
        player.write_end("I am loose 😭😭😭")
        return


    # Перевірка виграшу
    if player.touch_t(finish):
        player.write_end("I am wiin 😁😁😁")
        return


    # Повторний запуск функції через 100 мс (таймер)
    screen.ontimer(game, 100)


# --- Запуск гри ---
game()

done()
