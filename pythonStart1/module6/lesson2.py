class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):

    #запам'ятовуємо прямокутник:
        self.rect = pygame.Rect(x, y, width, height)
    # колір заливки - або переданий параметр, або загальний колір тла
        self.fill_color = color
        self.titles = []


    #додати текст до списку можливих написів
    def add_text(self, text):
        self.titles.append(text)


    #Встановити текст
    def set_text(self, number=0, fsize=20, text_color=BLACK):
        self.text = self.titles[number]
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)



    #Опис прямокутника з текстом
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))


