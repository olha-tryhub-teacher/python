import pygame
import functools
import time
from abc import ABC, abstractmethod

pygame.init()

# ---------- Decorator for logging ----------
def log_event(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{time.strftime('%H:%M:%S')}] Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# ---------- Constants ----------
WIDTH, HEIGHT = 500, 500
FPS = 40
BACKGROUND = (200, 255, 255)
PLATFORM_COLOR = (100, 100, 255)
BALL_COLOR = (255, 50, 50)
ENEMY_COLOR = (0, 150, 0)
TEXT_COLOR = (0, 0, 0)

# ---------- Abstract Drawable ----------
class Drawable(ABC):
    @abstractmethod
    def draw(self, surface):
        pass

# ---------- GameObject Base Class ----------
class GameObject(Drawable):
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)

# ---------- Label ----------
class Label(GameObject):
    def __init__(self, x, y, width, height, text='', fsize=36, text_color=TEXT_COLOR):
        super().__init__(x, y, width, height, BACKGROUND)
        self.text = text
        self.fsize = fsize
        self.text_color = text_color

    def draw(self, surface):
        super().draw(surface)
        font = pygame.font.SysFont('verdana', self.fsize)
        image = font.render(self.text, True, self.text_color)
        surface.blit(image, (self.rect.x + 10, self.rect.y + 10))


# ---------- Game Controller (Singleton Pattern) ----------
class GameController:
    _instance = None

    # реалізує патерн Singleton — щоб у грі був лише один контролер,
    # навіть якщо викликати GameController() кілька разів
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.init_game()

    def init_game(self):
        self.platform = GameObject(200, 300, 100, 30, PLATFORM_COLOR)
        self.ball = GameObject(160, 200, 20, 20, BALL_COLOR)
        self.dx, self.dy = 3, 3
        self.move_left = False
        self.move_right = False
        self.enemies = list(self.generate_enemies())

    @log_event
    def generate_enemies(self):
        for j in range(3):
            y = 5 + j * 55
            x = 5 + j * 27.5
            for i in range(9 - j):
                yield GameObject(x + i * 55, y, 50, 30, ENEMY_COLOR)

    @log_event
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_left = True
                elif event.key == pygame.K_d:
                    self.move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.move_left = False
                elif event.key == pygame.K_d:
                    self.move_right = False

    @log_event
    def update(self):
        if self.move_left:
            self.platform.rect.x -= 5
        if self.move_right:
            self.platform.rect.x += 5

        self.ball.rect.x += self.dx
        self.ball.rect.y += self.dy

        if self.ball.rect.left <= 0 or self.ball.rect.right >= WIDTH:
            self.dx *= -1
        if self.ball.rect.top <= 0:
            self.dy *= -1

        if self.ball.collides_with(self.platform):
            self.dy *= -1

        for enemy in self.enemies[:]:
            if self.ball.collides_with(enemy):
                self.enemies.remove(enemy)
                self.dy *= -1

    def draw_all(self):
        self.window.fill(BACKGROUND)
        self.platform.draw(self.window)
        self.ball.draw(self.window)
        for enemy in self.enemies:
            enemy.draw(self.window)

    def display_end_message(self, text, color):
        label = Label(150, 150, 200, 100, text=text, fsize=48, text_color=color)
        label.draw(self.window)
        pygame.display.update()
        pygame.time.wait(2000)

    def check_end_conditions(self):
        if self.ball.rect.top > HEIGHT:
            self.display_end_message("YOU LOSE", (255, 0, 0))
            self.running = False
        elif not self.enemies:
            self.display_end_message("YOU WIN", (0, 200, 0))
            self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw_all()
            self.check_end_conditions()
            pygame.display.update()
            self.clock.tick(FPS)

# ---------- Entry Point ----------
if __name__ == '__main__':
    game = GameController()
    game.run()
