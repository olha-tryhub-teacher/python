import time

from pygame import *

init()

size = 1000, 700
window = display.set_mode(size)
display.set_caption("Моя перша гра на 2 курсі на пайгеймі")
clock = time.Clock()



while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    display.update()
    clock.tick(50)

