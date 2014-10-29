#Author     : sakura_kyon@hotmail.com
#Question   : Spiral Matrix II
#Link       : https://oj.leetcode.com/problems/spiral-matrix-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 180 ms
#Description: 
#Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#For example,
#Given n = `3`,
#You should return the following matrix:
#```
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]
#```
#Show Tags
#Array

#Code       : 
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[None for _ in range(n)] for __ in range(n)]
        pos = (-1, 0)
        move = (1, 0)
        step = 0
        while 1:
            nx, ny = new_pos = pos[0] + move[0], pos[1] + move[1]
            if nx >= n or nx < 0 or ny >= n or ny <0 or not matrix[ny][nx] is None:
                move = -move[1], move[0]
                nx, ny = new_pos = pos[0] + move[0], pos[1] + move[1]
            if nx >= n or nx < 0 or ny >= n or ny <0 or not matrix[ny][nx] is None:
                break
            x, y = pos = new_pos
            step += 1
            matrix[y][x] = step
        return matrix
            