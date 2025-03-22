        # перевірка зіткнення кулі та монстрів (і монстр, і куля при зіткненні зникають)⬅️⬅️⬅️
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # цей цикл повториться стільки разів, скільки монстрів збито⬅️⬅️⬅️
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80),
                            -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # можливий програш: пропустили занадто багато або герой зіткнувся з ворогом⬅️⬅️⬅️
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True  # програли, ставимо тло і більше не керуємо спрайтами.⬅️⬅️⬅️
            window.blit(lose, (200, 200))

        # перевірка виграшу: скільки очок набрали?⬅️⬅️⬅️
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
