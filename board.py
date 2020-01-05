
class Board:
    def __init__(self):
        self.board = [[0 for cell in range(9)] for row in range(9)]

    def __str__(self):
        return self.make_printable()

    def make_printable(self):
        # Fix variable names. // Uncle Bob rules XD
        print('    A   B   C   D   E   F   G   H   I')
        c_gap = ' : '
        cx_gap = ' | '
        r_gap = '   ----------- ----------- ----------- '
        rx_gap = '   =========== =========== =========== ' 
        string_table = rx_gap + '\n'
        row_label = 1
        for row_index, row in enumerate(self.board):
            string_table += ' ' + str(row_label) + cx_gap[1:]
            for e_index, elem in enumerate(row):
                if e_index == 2 or e_index == 5 or e_index == 8:
                    string_table += (str(elem) + cx_gap)
                else:
                    string_table += (str(elem) + c_gap)

            norm_gap = '\n' + r_gap + '\n'
            sep_gap = '\n' + rx_gap + '\n'
            if row_index == 2 or row_index == 5 or row_index == 8:
                string_table += sep_gap
            else:
                string_table += norm_gap

            row_label += 1
        return string_table 

    def load(self, puzzle: str):
        # Load existing sudoku puzzle to board
        self.board = [[data if data != '0' else ' ' for data in puzzle[i*9:(i*9)+9]] for i in range(9)]

b = Board()
b.load('005910308009403060027500100030000201000820007006007004000080000640150700890000420')
print(b)

