#Author     : sakura_kyon@hotmail.com
#Question   : Valid Sudoku
#Link       : https://oj.leetcode.com/problems/valid-sudoku/
#Language   : python
#Status     : Accepted
#Run Time   : 360 ms
#Description: 
#Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).
#The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.
#A partially filled sudoku which is valid.
####Note:###
#A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#Show Tags
#Hash Table

#Code       : 
def check(elems):
    flags = [0 for _ in xrange(9)]
    for e in elems:
        if e == '.':
            continue
        elif e < 0 or e > 9 or flags[e - 1] > 0:
            return False
        else:
            flags[e - 1] += 1
    return True

def get_row(board, index):
    return board[index]
    
def get_col(board, index):
    for row in board:
        yield row[index]

def get_box(board, index):
    frow = index % 3
    fcol = index / 3
    for y in xrange(3):
        row = board[frow * 3 + y]
        for x in xrange(3):
            yield row[fcol * 3 + x]

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        board = [[int(e) if '0' <= e <= '9' else e for e in row] for row in board]
        return all(check(get_row(board, i)) and check(get_col(board, i)) and check(get_box(board, i)) for i in range(9))