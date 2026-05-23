from pygame import *

init()

size = 1000, 800
window = display.set_mode(size)
display.set_caption('Моя гра')
clock = time.Clock()

player = Rect(200, 200, 50, 50)
player_speed = 5

while True:
    for e in event.get():
       if e.type == QUIT:
           quit()

    keys = key.get_pressed()
    if keys[K_w]:
        player.y -= player_speed
    if keys[K_s]:
        player.y += player_speed
    if keys[K_a]:
        player.x -= player_speed
    if keys[K_d]:
        player.x += player_speed

    window.fill((255, 255, 255))
    draw.rect(window, (0, 200, 0), player)

    display.update()
    clock.tick(60)
