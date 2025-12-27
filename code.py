    # Кульки
    to_remove = []
    for ball in balls:
        if player.collidecircle(ball):
            to_remove.append(ball)
            player.radius += int(ball.radius * 0.2)
        else:
            ball.reset(player.x, player.y, scale)

    for ball in to_remove:
        balls.remove(ball)
