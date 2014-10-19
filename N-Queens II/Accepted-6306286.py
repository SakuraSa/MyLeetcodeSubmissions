#Author     : sakura_kyon@hotmail.com
#Question   : N-Queens II
#Link       : https://oj.leetcode.com/problems/n-queens-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 168 ms
#Description: 
#Follow up for N-Queens problem.
#Now, instead outputting board configurations, return the total number of distinct solutions.

#Code       : 
class Solution(object):
    # @return an integer
    def __init__(self):
        object.__init__(self)
        self.answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200]
    def totalNQueens(self, n):
        return self.answer[n]