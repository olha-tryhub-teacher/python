for j in range(3):  # цикл по стовпцях
    y = start_y + (55 * j)  # координата монстра у кожному слід. стовпці буде зміщена на 55 пікселів по y
    x = start_x + (27.5 * j)  # і 27.5 по x
    for i in range(count):  # цикл по рядах(рядків) створює в рядку кількість монстрів,що дорівнює count
        d = Picture('enemy.png', x, y, 50, 50)  # створюємо монстра
        monsters.append(d)  # додаємо до списку
        x = x + 55  # збільшуємо координату наступного монстра
    count = count - 1  # для наступного ряду зменшуємо кількість монстрів

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # малюємо всіх монстрів зі списку
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
