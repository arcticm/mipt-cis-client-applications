import pygame
from .constants import FONT


class Button(pygame.sprite.Sprite):

    def __init__(self, win, x, y, width, height, text_color, background_color, text, time=None):
        super().__init__()

        self.win = win
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.time = time

    @staticmethod
    def drawTextcenter(text, font, screen, x, y, color):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=(int(x), int(y)))
        screen.blit(textobj, textrect)

    def draw(self):
        pygame.draw.rect(self.win, self.background_color, (self.rect), 0)
        self.drawTextcenter(self.text, FONT, self.win, self.x + self.width / 2, self.y + self.height / 2, self.text_color)
        pygame.draw.rect(self.win, self.text_color, self.rect, 3)

    def clicked(self, pos, time):
        if self.rect.collidepoint(pos):
            if self.time is None:
                self.time = pygame.time.get_ticks()
                return True
            elif time - self.time > 1000:
                self.time = time
                return True
        return False