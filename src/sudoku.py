
class Sudoku:
    def __init__(self):
        self.col = '123456789'
        self.row = 'ABCDEFGHI'
        self.squares = self.cross(self.row, self.col)
        unitlist = ([self.cross(self.row, c) for c in self.col] +
            [self.cross(r, self.col) for r in self.row] +
            [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        self.units = dict((s, [u for u in unitlist if s in u]) 
             for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
             for s in self.squares)

    def cross(self, A, B):
        return [a+b for a in A for b in B]

    def start(self):
        pass


s = Sudoku()
print(s.units['A1'])
#print(s.peers)
