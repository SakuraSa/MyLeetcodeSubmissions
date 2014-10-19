#Author     : sakura_kyon@hotmail.com
#Question   : Sudoku Solver
#Link       : https://oj.leetcode.com/problems/sudoku-solver/
#Language   : python
#Status     : Accepted
#Run Time   : 228 ms
#Description: 
#Write a program to solve a Sudoku puzzle by filling the empty cells.
#Empty cells are indicated by the character `'.'`.
#You may assume that there will be only one unique solution.
#A sudoku puzzle...
#...and its solution numbers marked in red.

#Code       : 
def cross(collection0, collection1):
    """Cross product of elements in A and elements in B."""
    return [a + b for a in collection0 for b in collection1]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s], [])) - {s})
             for s in squares)
             

################ Parse a Grid ################


def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            ## (Fail if we can't assign d to square s.)
            return False
    return values


def grid_values(grid):
    """Convert grid into a dict of {square: char} with '0' or '.' for empties."""
    chars = [char for char in grid if char in digits or char in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))


################ Constraint Propagation ################


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        ## Already eliminated
        return values
    values[s] = values[s].replace(d, '')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        ## Contradiction: removed last value
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for unit in units[s]:
        d_places = [s for s in unit if d in values[s]]
        if len(d_places) == 0:
             ## Contradiction: no place for this value
            return False
        elif len(d_places) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, d_places[0], d):
                return False
    return values


################ Search ################

def solve(grid):
    return search(parse_grid(grid))


def search(values):
    """Using depth-first search and propagation, try all possible values."""
    if values is False:
        ## Failed earlier
        return False
    if all(len(values[s]) == 1 for s in squares):
        ## Solved!
        return values
    ## Chose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])


################ Utilities ################

def some(seq):
    """Return some element of seq that is true."""
    for e in seq:
        if e:
            return e
    return False


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        grid = "".join("".join(map(str, row)) for row in board)
        for key, value in solve(grid).iteritems():
            row = rows.index(key[0])
            col = cols.index(key[1])
            board[row][col] = value
        