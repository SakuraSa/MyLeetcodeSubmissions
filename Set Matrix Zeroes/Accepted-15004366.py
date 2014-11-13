#Author     : sakura_kyon@hotmail.com
#Question   : Set Matrix Zeroes
#Link       : https://oj.leetcode.com/problems/set-matrix-zeroes/
#Language   : python
#Status     : Accepted
#Run Time   : 668 ms
#Description: 
#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#[click to show follow up.](#)
####Follow up:###
#Did you use extra space?
#A straight forward solution using O(mn) space is probably a bad idea.
#A simple improvement uses O(m + n) space, but still not the best solution.
#Could you devise a constant space solution?
#Show Tags
#Array

#Code       : 
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        zero_row = set([
            index 
            for index, row in enumerate(matrix) 
            if any(i == 0 for i in row)
        ])
        zero_col = set([
            index 
            for index in range(len(matrix[0])) 
            if any(row[index] == 0 for row in matrix)
        ])
        for x, row in enumerate(matrix):
            for y in range(len(row)):
                if x in zero_row or y in zero_col:
                    row[y] = 0