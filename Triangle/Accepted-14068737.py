#Author     : sakura_kyon@hotmail.com
#Question   : Triangle
#Link       : https://oj.leetcode.com/problems/triangle/
#Language   : python
#Status     : Accepted
#Run Time   : 276 ms
#Description: 
#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#For example, given the following triangle
#```
#[
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
#]
#```
#The minimum path sum from top to bottom is `11` (i.e., 2 + 3 + 5 + 1 = 11).
####Note:###
#Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for layer in range(1, len(triangle)):
            last_row = triangle[layer - 1]
            row = triangle[layer]
            for index in range(len(row)):
                left = right = 10000000000
                if index > 0:
                    left = last_row[index - 1]
                if index < len(last_row):
                    right = last_row[index]
                row[index] = min(left, right) + row[index]
        return min(triangle[-1])