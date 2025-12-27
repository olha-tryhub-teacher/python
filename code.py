    # ⬇️⬇️⬇️
    def draw_center(self, scale):
        draw.circle(
            window,
            self.color,
            (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2),
            int(self.radius * scale)
        )
