running = True
while running:
    window.fill((255, 255, 255))
    diff_text = main_font.render("Складність: " + difficulties[current_index], True, (0, 0, 0))
    window.blit(diff_text, (180, 20))
    play_button.draw()
    settings_button.draw()
    exit_button.draw()

    display.update()

    for e in event.get():
        if e.type == QUIT:
            running = False
        if play_button.is_clicked(e):
            print("Гра запускається зі складністю:", difficulties[current_index])
        if settings_button.is_clicked(e):
            current_index = (current_index + 1) % len(difficulties)
            with open(filename, "w") as f:
                json.dump({"difficulty": difficulties[current_index]}, f)
        if exit_button.is_clicked(e):
            print("Вихід...")
            running = False
