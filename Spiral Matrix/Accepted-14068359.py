#Author     : sakura_kyon@hotmail.com
#Question   : Spiral Matrix
#Link       : https://oj.leetcode.com/problems/spiral-matrix/
#Language   : python
#Status     : Accepted
#Run Time   : 132 ms
#Description: 
#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#For example,
#Given the following matrix:
#```
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#```
#You should return `[1,2,3,6,9,8,7,4,5]`.
#Show Tags
#Array

#Code       : 
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix[0])
        n = len(matrix)
        res = []
        pos = (-1, 0)
        move = (1, 0)
        while 1:
            nx, ny = new_pos = pos[0] + move[0], pos[1] + move[1]
            if nx >= m or nx < 0 or ny >= n or ny <0 or matrix[ny][nx] is None:
                move = -move[1], move[0]
                nx, ny = new_pos = pos[0] + move[0], pos[1] + move[1]
            if nx >= m or nx < 0 or ny >= n or ny <0 or matrix[ny][nx] is None:
                break
            x, y = pos = new_pos
            res.append(matrix[y][x])
            matrix[y][x] = None
        return res