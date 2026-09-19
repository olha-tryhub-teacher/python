        if event.type == pygame.MOUSEBUTTONDOWN and (
                (event.pos[0] - self.circle_x) ** 2 + (
                event.pos[1] - self.rect.centery) ** 2
        ) ** 0.5 < 15:
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if self.dragging and event.type == pygame.MOUSEMOTION:
            # Обмежуємо рух повзунка межами слайдера
            self.circle_x = max(self.rect.left,
                                min(event.pos[0], self.rect.right))
            self.val = (self.circle_x - self.rect.x) / self.rect.width
            return True  # Повертаємо True, щоб знати, що гучність змінилася
        return False
