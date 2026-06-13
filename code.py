while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    window.fill((40, 40, 40))

    if not lose:
        ball.update_player(cells)
        # Відправка своїх координат на сервер
        sock.send(f"{my_id},{int(ball.x)},{int(ball.y)},{int(ball.radius)},Player".encode())

    # Малювання яблук
    for cell in cells:
        cell.draw(window, ball.x, ball.y, ball.scale)

    # Малювання ворогів
    for pid, data in all_players.items():
        # Малюємо ворога як червоне коло
        ox, oy, orad = data
        sx = int((ox - ball.x) * ball.scale + size[0] // 2)
        sy = int((oy - ball.y) * ball.scale + size[1] // 2)
        draw.circle(window, (255, 50, 50), (sx, sy), max(4, int(orad * ball.scale)))

    if not lose:
        ball.draw(window, ball.x, ball.y, 1.0 if ball.radius < 60 else ball.scale)
    else:
        window.blit(f.render("U lose!", 1, (244, 0, 0)), (400, 500))

    display.update()
    clock.tick(60)

quit()
