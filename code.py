    # перевірка програшу
    if ball.rect.top > HEIGHT:
        label_lose.draw(screen)  # ⬅️
        running = False

    if len(blocks) == 0:  # ⬅️
        label_win.draw(screen)  # ⬅️
        running = False  # ⬅️
