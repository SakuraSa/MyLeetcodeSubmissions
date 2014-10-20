#Author     : sakura_kyon@hotmail.com
#Question   : Surrounded Regions
#Link       : https://oj.leetcode.com/problems/surrounded-regions/
#Language   : python
#Status     : Accepted
#Run Time   : 892 ms
#Description: 
#Given a 2D board containing `'X'` and `'O'`, capture all regions surrounded by `'X'`.
#A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.
#For example,
#```
#X X X X
#X O O X
#X X O X
#X O X X
#```
#After running your function, the board should be:
#```
#X X X X
#X X X X
#X X X X
#X O X X
#```
#Show Tags
#Breadth-first Search

#Code       : 
class Board(object):
    def __init__(self, board):
        self.board = board
        self.size = (len(board[0]), len(board))
        self.move = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

    def run(self):
        stack = []
        mem = set()
        surrounded = [
            [False for _ in row]
            for row in self.board
        ]
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == "O" and (
                    x == 0 or y == 0 or x == self.size[0] - 1 or y == self.size[1] - 1):
                    stack.append((x, y))
        while stack:
            x, y = pos = stack.pop()
            cell = self.board[y][x]
            if pos in mem:
                continue
            else:
                mem.add(pos)
            if x == 0 or y == 0 or x == self.size[0] - 1 or y == self.size[1] - 1:
                surrounded[y][x] = True
            for move in self.move:
                npos = nx, ny = x + move[0], y + move[1]
                if nx < 0 or ny < 0 or nx >= self.size[0] or ny >= self.size[1]:
                    continue
                if surrounded[ny][nx]:
                    surrounded[y][x] = True
                elif self.board[ny][nx] == "O":
                    stack.append(npos)
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == "O" and surrounded[y][x] == False:
                    self.board[y][x] = "X"

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board:
            Board(board).run()
        