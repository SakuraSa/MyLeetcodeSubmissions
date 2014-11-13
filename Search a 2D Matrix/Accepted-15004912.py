#Author     : sakura_kyon@hotmail.com
#Question   : Search a 2D Matrix
#Link       : https://oj.leetcode.com/problems/search-a-2d-matrix/
#Language   : python
#Status     : Accepted
#Run Time   : 256 ms
#Description: 
#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#* Integers in each row are sorted from left to right.
#* The first integer of each row is greater than the last integer of the previous row.
#For example,
#Consider the following matrix:
#```
#[
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
#]
#```
#Given ###target### = `3`, return `true`.
#Show Tags
#ArrayBinary Search

#Code       : 
def searchRow(matrix, target, begain=0, end=None):
    if end is None:
        end = len(matrix) -1
    if begain == end:
        row = matrix[begain]
        if row[0] <= target <= row[-1]:
            return row
        else:
            return False
    elif begain < end:
        if target < matrix[begain][0] or target > matrix[end][-1]:
            return False
        mid = (begain + end) / 2
        row = matrix[mid]
        if row[0] <= target <= row[-1]:
            return row
        if target < row[0]:
            return searchRow(matrix, target, begain, mid - 1)
        elif row[-1] < target:
            return searchRow(matrix, target, mid + 1, end)
    return False

def half(row, target, begain=0, end=None):
    if end is None:
        end = len(row) - 1
    if begain == end:
        return row[begain] == target
    elif begain < end:
        if target < row[begain] or target > row[end]:
            return False
        mid = (begain + end) / 2
        if row[mid] == target:
            return True
        elif target < row[mid]:
            return half(row, target, begain, mid - 1)
        else:
            return half(row, target, mid + 1, end)
    return False

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        row = searchRow(matrix, target)
        return row and half(row, target)
        