from solver.nolvig import Nolvig
from src.board import Board

class Sudoku:
    def __init__(self):
        pass

    def start(self):
        b = Board()
        b.load('400000805030000000000700000020000060000080400000010000000603070500200000104000000')
        solver = Nolvig()
        b.load(b.grid)
        solver.solve(b.grid)
        print(b)


#s = Sudoku()
#print(s.units['A1'])
#print(s.peers)
