from pygame import *

init()

size = 500, 500

window = display.set_mode(size)
display.set_caption("ВАША НАЗВА")
clock = time.Clock()

# bg = image.load("img.png")
# bg = transform.scale(bg, size)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    # window.blit(bg, (0, 0))

    display.update()
    clock.tick(60)
