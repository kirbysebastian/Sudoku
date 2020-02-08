
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
        for i in range(9):
            row_text = '{} '.format(i+1)
            for j in range(9):
                col_index = j + (i*9)
                char_d = self.grid[col_index]
                if self.grid[col_index] == '0':
                    char_d = '.'

                row_text = row_text + ' ' + char_d + ' '
                if (j+1)%3 == 0 and (j+1) != 9:
                    row_text = row_text + '|'

            table_str = table_str + row_text + '\n'
            if (i+1)%3 == 0 and (i+1) != 9:
                table_str += '  ---------|---------|---------' + '\n'

        return table_str

    def load(self, puzzle: str):
        # Load existing sudoku puzzle to board
        self.grid = puzzle
        self.board = [[data if data != '0' else ' ' for data in self.grid[i*9:(i*9)+9]] for i in range(9)]
        #print(self.board)


