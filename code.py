class MyRect():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 200, 50)
        # створення активної та пасивної поверхней
        # створення поверхонь
        self.normal_surf = pygame.Surface((self.rect.width, self.rect.height))
        self.normal_surf.fill(BLUE)

        self.hover_surf = pygame.Surface((self.rect.width, self.rect.height))
        self.hover_surf.fill(RED)

        self.current_surf = self.normal_surf

    def update(self):
        # перевірка, чи курсор мишки над прямокутником
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.current_surf = self.hover_surf
        else:
            self.current_surf = self.normal_surf

    def draw(self, surface):
        # відмальовка потрібної поверхні
        surface.blit(self.current_surf, (self.rect.x, self.rect.y))


#######################################
# об'єкт прямокутника, потрібно його створити
r = MyRect(100, 100)
