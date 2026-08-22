from pygame import *
import socket
import json
from threading import Thread

# ---ПУГАМЕ НАЛАШТУВАННЯ ---
WIDTH, HEIGHT = 800, 600
init()
screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption("Пінг-Понг")
# ---СЕРВЕР ---
def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('localhost', 8080)) # ---- Підключення до сервера
            buffer = ""
            game_state = {}
            my_id = int(client.recv(24).decode())
            return my_id, game_state, buffer, client
        except:
            pass


def receive():
    global buffer, game_state, game_over
    while not game_over:
        try:
            data = client.recv(1024).decode()
            buffer += data
            while "\n" in buffer:
                packet, buffer = buffer.split("\n", 1)
                if packet.strip():
                    game_state = json.loads(packet)
        except:
            game_state["winner"] = -1
            break

# --- ШРИФТИ ---
font_win = font.Font(None, 72)
font_main = font.Font(None, 36)
# --- ЗОБРАЖЕННЯ ----
loading_bg = image.load("images/loading.png")
loading_bg = transform.scale(loading_bg, (WIDTH, HEIGHT))

start_game = image.load("images/start-game.jpg")
start_game = transform.scale(start_game, (WIDTH, HEIGHT))

game_bg = image.load("images/football-field.webp")
game_bg = transform.scale(game_bg, (WIDTH, HEIGHT))

win_bg = image.load("images/you-are-winner.jpg")
win_bg = transform.scale(win_bg, (WIDTH, HEIGHT))

lose_bg = image.load("images/you-lose-game.jpg")
lose_bg = transform.scale(lose_bg, (WIDTH, HEIGHT))

ball_img = image.load("images/c526aa7a72e56853621ec7eb78642e53.png")
ball_img = transform.scale(ball_img, (20, 20))
# --- ЗВУКИ ---
mixer.music.load("Song/Hero Immortal.mp3")
mixer.music.play(-1)

ball_platform_sound = mixer.Sound("Song/#2.wav")

ball_wall_sound = mixer.Sound("Song/swish_2.wav")

# pause() — пауза
# unpause() — продовжити
# stop() — зупинка
# --- ГРА ---
game_over = False
winner = None
you_winner = None
my_id, game_state, buffer, client = connect_to_server()
Thread(target=receive, daemon=True).start()
while True:
    for e in event.get():
        if e.type == QUIT:
            exit()

    if "countdown" in game_state and game_state["countdown"] > 0:
        # screen.fill((0, 0, 0))
        screen.blit(start_game, (0, 0))
        countdown_text = font.Font(None, 72).render(str(game_state["countdown"]), True, (255, 255, 255))
        screen.blit(countdown_text, (WIDTH // 2 - 20, HEIGHT // 2 - 30))
        display.update()
        continue  # Не малюємо гру до завершення відліку

    if "winner" in game_state and game_state["winner"] is not None:
        screen.fill((20, 20, 20))

        if you_winner is None:  # Встановлюємо тільки один раз
            if game_state["winner"] == my_id:
                you_winner = True
            else:
                you_winner = False

        if you_winner:
            text = "Ти переміг!"
            end_bg = win_bg
        else:
            text = "Пощастить наступним разом!"
            end_bg = lose_bg

        win_text = font_win.render(text, True, (255, 215, 0))
        text_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(end_bg, (0, 0))
        screen.blit(win_text, text_rect)

        text = font_win.render('К - рестарт', True, (255, 215, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
        screen.blit(text, text_rect)

        display.update()
        continue  # Блокує гру після перемоги

    if game_state:
        # screen.fill((30, 30, 30))
        screen.blit(game_bg, (0, 0))
        draw.rect(screen, (0, 255, 0), (20, game_state['paddles']['0'], 20, 100))
        draw.rect(screen, (255, 0, 255), (WIDTH - 40, game_state['paddles']['1'], 20, 100))
        draw.circle(screen, (255, 255, 255), (game_state['ball']['x'], game_state['ball']['y']), 10)
        screen.blit(ball_img, (game_state['ball']['x'] + 10, game_state['ball']['y'] + 10))
        score_text = font_main.render(f"{game_state['scores'][0]} : {game_state['scores'][1]}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 -25, 20))

        if game_state['sound_event']:
            if game_state['sound_event'] == 'wall_hit':
                # звук відбиття м'ячика від стін
                ball_wall_sound.play()
            if game_state['sound_event'] == 'platform_hit':
                # звук відбиття м'ячика від платформи
                ball_platform_sound.play()

    else:
        wating_text = font_main.render(f"Очікування гравців...", True, (255, 255, 255))
        screen.blit(loading_bg, (0, 0))
        screen.blit(wating_text, (WIDTH // 2 - 25, 20))

    display.update()
    clock.tick(60)

    keys = key.get_pressed()
    if keys[K_w]:
        client.send(b"UP")
    elif keys[K_s]:
        client.send(b"DOWN")
