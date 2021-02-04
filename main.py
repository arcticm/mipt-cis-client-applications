import pygame, time
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE, GREY, BIG_FONT
from checkers.game import Game
from checkers.button import Button

FPS = 60
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(GREY)
pygame.display.set_caption('Checkers')

b1 = Button(WIN, 850, 200, 300, 50, BLACK, WHITE, 'New Game')
b2 = Button(WIN, 850, 275, 300, 50, BLACK, WHITE, 'Quit')
menu = pygame.sprite.Group()

for btn in [b1, b2]:
    btn.draw()
    menu.add(btn)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def congratulate(win, color):
    background = pygame.Surface((800, 1200))
    background.fill(BLACK)
    win.blit(background, (0, 0))
    sentence = BIG_FONT.render(color + ' Wins!', True, WHITE, GREY)
    sentenceRect = sentence.get_rect()
    sentenceRect.center = (400, 400)
    win.blit(sentence, sentenceRect)
    pygame.display.update()
    time.sleep(5)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            congratulate(WIN, game.winner_color())
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                frame = pygame.time.get_ticks()
                if col <= 7:
                	game.select(row, col)
                else:
                	for i in menu:
                		if i.clicked(pos, frame):
                			if i.text == "New Game":
                				game.reset()
                			elif i.text == "Quit":
                				pygame.quit()

        game.update()
    
    pygame.quit()

if __name__ == '__main__':
	main()
