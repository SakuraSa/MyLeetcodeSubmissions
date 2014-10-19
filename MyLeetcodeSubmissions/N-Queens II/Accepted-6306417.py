#Author     : sakura_kyon@hotmail.com
#Question   : N-Queens II
#Link       : https://oj.leetcode.com/problems/n-queens-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 424 ms
#Description: 
#Follow up for N-Queens problem.
#Now, instead outputting board configurations, return the total number of distinct solutions.

#Code       : 
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.counter = 0
        self.solve(list(), n, self.catcher)
        return self.counter

    def catcher(self, answer):
        self.counter += 1

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