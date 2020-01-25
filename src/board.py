
'''
board = {
    'A':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'B':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'C':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'D':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'E':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'F':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'G':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'H':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'I':[1, 2, 3, 4, 5, 6, 7, 8, 9]
}
'''

class Board:
    def __init__(self):
        self.board = [[0 for cell in range(9)] for row in range(9)]

    def __str__(self):
        return self.make_printable()

    def make_printable(self):
        table_str = '   A  B  C   D  E  F   G  H  I' + '\n\n'
        for c, row in enumerate(self.board):
            row_text = '{} '.format(c+1)
            for i, d in enumerate(row):
                if d == ' ':
                    d = '.'

                row_text = row_text + ' ' + d + ' '
                if (i+1)%3 == 0 and (i+1) != 9:
                    row_text = row_text + '|'
            table_str += row_text + '\n'
            if (c+1)%3 == 0 and (c+1) != 9:
                table_str += '  ---------|---------|---------' + '\n'
        return table_str


    def load(self, puzzle: str):
        # Load existing sudoku puzzle to board
        self.board = [[data if data != '0' else ' ' for data in puzzle[i*9:(i*9)+9]] for i in range(9)]

b = Board()
#b.load('005910308009403060027500100030000201000820007006007004000080000640150700890000420')
b.load('400000805030000000000700000020000060000080400000010000000603070500200000104000000')
print(b)

