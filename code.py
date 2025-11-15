    ball.update()
    player.update()

    # перевірка програшу
    if ball.rect.top > HEIGHT:
        print("Game Over!")
        running = False

    if player.collide(ball):
        ball.change_velocity(player)

    screen.blit(image_bg, (0, 0))

    for b in blocks[:]:
        if b.collide(ball):
            blocks.remove(b)
            ball.velocityy = ball.SPEED
            score += 100
            label.set_text(f"Score: {score}")
        b.draw(screen)

    ball.draw(screen)
    label.draw(screen)
    player.draw(screen)
