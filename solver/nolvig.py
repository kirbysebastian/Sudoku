from solver.solver import Solver

# Based on Peter Nolvig's solver algorithm
# Link: https://norvig.com/sudoku.html

class Nolvig(Solver):
    def __init__(self):
        self.digits = '123456789'
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
        self.squares = [a+b for a in 'ABCDEFGHI' for b in '123456789']
        super().__init__()

    def solve(self, grid):
        done = self.search(self.parse_grid(grid))
        #self.display(done)
        return done

    def cross(self, A, B):
        return [a+b for a in A for b in B]

    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        ## To start, every square can be any digit; then assign values from the grid.
        values = dict((s, self.digits) for s in self.squares)
        for s,d in self.grid_values(grid).items():
            if d in self.digits and not self.assign(values, s, d):
                return False ## (Fail if we can't assign d to square s.)
        return values

    def grid_values(self, grid):
        #Convert grid into a dict of {square: char} with '0' or '.' for empties.
        chars = [c for c in grid if c in self.digits or c in '0.']
        print(chars)
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def search(self, values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False ## Failed earlier
        if all(len(values[s]) == 1 for s in self.squares): 
            return values ## Solved!
        ## Chose the unfilled square s with the fewest possibilities
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d)) 
            for d in values[s])

    def some(self, seq):
        "Return some element of seq that is true."
        for e in seq:
            if e: return e
        return False

    def assign(self, values, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values ## Already eliminated
        values[s] = values[s].replace(d,'')
        ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
        if len(values[s]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        ## (2) If a unit u is reduced to only one place for a value d, then put it there.
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def display(self, values):
        "Display these values as a 2-D grid."
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.row:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                          for c in self.col))
            if r in 'CF': print(line)


