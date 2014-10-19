#Author     : sakura_kyon@hotmail.com
#Question   : N-Queens
#Link       : https://oj.leetcode.com/problems/n-queens/
#Language   : python
#Status     : Accepted
#Run Time   : 472 ms
#Description: 
#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#Given an integer n, return all distinct solutions to the n-queens puzzle.
#Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.
#For example,
#There exist two distinct solutions to the 4-queens puzzle:
#```
#[
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],
# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
#```

#Code       : 
class Solution:
    # @return an integer
    def solveNQueens(self, n):
        self.counter = list()
        self.solve(list(), n, self.catcher)
        return self.counter

    def catcher(self, answer):
        an = list()
        n = len(answer)
        for i in answer:
            t = ["."] * n
            t[i] = "Q"
            an.append("".join(t))
        self.counter.append(an)

    def solve(self, board, n, catcher):
        line = len(board)
        if line >= n:
            catcher(board)
        else:
            for i in range(n):
                canPut = True
                for j in range(line):
                    if i == board[j] or abs(line - j) == abs(i - board[j]):
                        canPut = False
                        break
                if canPut:
                    board.append(i)
                    self.solve(board, n, catcher)
                    board.pop()