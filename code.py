import pygame as pg

BLACK = (0, 0, 0)
WIDTH = 500
HEIGHT = 500

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

# завантаження картинок
image_ball = pg.image.load("Ball.png").convert_alpha()
image_block1 = pg.image.load("Block1.png").convert_alpha()
image_block2 = pg.image.load("Block2.png").convert_alpha()
image_block3 = pg.image.load("Block3.png").convert_alpha()
image_platform1 = pg.image.load("Platform1.png").convert_alpha()
image_bg = pg.image.load("background.png").convert()
