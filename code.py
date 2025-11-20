# створюємо шрифт
font = pygame.font.Font(None, 48)
font.set_italic(True)
font.set_bold(True)
# створення поверхні із текстом
text_image = font.render("Hello, world!", True, YELLOW)
