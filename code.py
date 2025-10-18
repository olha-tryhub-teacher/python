from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
pressed_keys = set()

running = True
while running:
    screen.fill(WHITE)

    # клавіші
    draw_keys(screen, key_rects, pressed_keys)

    display.flip()

    for e in event.get():
        if e.type == QUIT:
            running = False

        # клавіатура
        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)

        # миша по клавішах
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)

        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)
