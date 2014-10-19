#Author     : sakura_kyon@hotmail.com
#Question   : Rotate Image
#Link       : https://oj.leetcode.com/problems/rotate-image/
#Language   : python
#Status     : Accepted
#Run Time   : 208 ms
#Description: 
#You are given an n x n 2D matrix representing an image.
#Rotate the image by 90 degrees (clockwise).
#Follow up:
#Could you do this in-place?

#Code       : 
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        size = len(matrix)
        return [
            [
                matrix[size - 1 - y][x]
                for y in range(size)    
            ]
            for x in range(size)
        ]