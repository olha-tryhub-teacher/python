    # Вираховуємо масштабований розмір фону
    bg_scaled_size = int(WORLD_SIZE * ball.scale)
    scaled_bg = transform.scale(bg_img, (bg_scaled_size, bg_scaled_size))

    # Координата -2000 — це верхній лівий кут нашого основного світу
    base_bg_x = int((-2000 - ball.x) * ball.scale + size[0] // 2)
    base_bg_y = int((-2000 - ball.y) * ball.scale + size[1] // 2)

    # НОВЕ: Логіка нескінченного фону ("спавн" нових тайлів за краями)
    # Знаходимо найближчу до лівого верхнього кута екрану точку прив'язки фону.
    # Остача від ділення (%) забезпечує плавний перехід без розривів.
    start_x = (base_bg_x % bg_scaled_size) - bg_scaled_size
    start_y = (base_bg_y % bg_scaled_size) - bg_scaled_size
