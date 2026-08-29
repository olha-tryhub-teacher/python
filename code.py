    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        for p in self.pipes:
            self.draw_pipe(p['top'], True)
            self.draw_pipe(p['bot'])
        self.screen.blit(self.bird_img, self.bird)
        txt = self.font.render(str(self.score), True, 'white')
        self.screen.blit(txt, (WIDTH // 2, 50))
        if self.lose:
            msg = self.font.render("GAME OVER - Press 'R'", True, 'red')
            self.screen.blit(msg, (WIDTH // 2 - 300, HEIGHT // 2))

# --- ЗАПУСК ---
game = Game()
while True:
    game.update()
    game.draw()
    pg.display.update()

    for e in pg.event.get():
        if e.type == pg.QUIT: 
            exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE: # Стрибок на пробіл
                game.jump_action()
            if e.key == pg.K_r and game.lose: # Перезапуск
                game.reset()

    game.clock.tick(60)
