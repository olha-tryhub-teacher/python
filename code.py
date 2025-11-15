# створення об'єктів гри
ball = Ball(100, HEIGHT//2, image_ball, 4)
player = Player(WIDTH//2 - 50, HEIGHT - 60, image_platform1)

score = 0
label = TextLabel(370, 470, 28)
label.set_text(f"Score: {score}")

blocks = []
for i in range(15):
    row = i // 5
    col = i % 5
    blocks.append(Sprite(50 + col*80, 20 + row*40,
                  [image_block1, image_block2, image_block3][row]))
