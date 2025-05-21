if mode == "catch":
    for bonus in bonus_ships:
        if bonus.rect.collidepoint(x, y):
            coins += 1
            bonus.kill()
