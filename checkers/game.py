import pygame
from .constants import SQUARE_SIZE, ROWS, COLS, BLACK, WHITE, BLUE
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.get_piece(row, col)
                if piece != 0 and piece.color == self.turn:
                    if self.board.get_valid_moves(piece) != {}:
                        return None
        if self.turn == BLACK:
            return WHITE or self.board.winner()
        else:
            return BLACK or self.board.winner()

    def winner_color(self):
        if self.winner() == BLACK:
            return "BLACK"
        else:
            return "WHITE"

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            print(self.valid_moves)
            return True    
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE