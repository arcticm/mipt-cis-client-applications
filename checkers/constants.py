import pygame

WIDTH, HEIGHT = 1200, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = 800//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('media/crown.png'), (44, 25))

pygame.init()
FONT = pygame.font.Font('media/consola.ttf', 30)
BIG_FONT = pygame.font.Font('media/consola.ttf', 50)

