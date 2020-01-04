
class Board:
    def __init__(self):
        self.board = [[0 for cell in range(9)] for row in range(9)]

    def __str__(self):
        return self.make_printable()

    def make_printable(self):
        c_gap = ' | '
        r_gap = '------------------'
        return ''

    def load(self):
        # Load sudoku puzzle to board
        pass
