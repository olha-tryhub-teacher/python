class Ball:
    def __init__(self, x, y, radius, color, speed=0):
        self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.base_speed = speed
        self.scale = 1.0
        self.growth_limit = 60

    def update_player(self, cells):
        # Масштабування
        self.scale = self.growth_limit / self.radius if self.radius > self.growth_limit else 1.0

        keys = key.get_pressed()
        speed = 15 * self.scale
        if keys[K_UP]: self.y -= speed
        if keys[K_DOWN]: self.y += speed
        if keys[K_LEFT]: self.x -= speed
        if keys[K_RIGHT]: self.x += speed

        # Логіка поїдання (спрощено)
        for cell in cells[:]:
            if self.collidecircle(cell):
                self.radius += cell.radius * 0.2
                cells.remove(cell)

    def draw(self, surface, camera_x, camera_y, camera_scale):
        sx = int((self.x - camera_x) * camera_scale + size[0] // 2)
        sy = int((self.y - camera_y) * camera_scale + size[1] // 2)
        r = int(self.radius * camera_scale)
        draw.circle(surface, self.color, (sx, sy), max(2, r))

    def collidecircle(self, ball2):
        distance = hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)
