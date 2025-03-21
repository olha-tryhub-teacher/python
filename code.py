YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)

cards = []
num_cards = 4

x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 14)
    cards.append(new_card)
    x = x + 100

while True:
    for card in cards:
        card.draw(10, 30)

    display.update()
    clock.tick(40)
