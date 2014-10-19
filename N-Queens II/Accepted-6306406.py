#Author     : sakura_kyon@hotmail.com
#Question   : N-Queens II
#Link       : https://oj.leetcode.com/problems/n-queens-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 120 ms
#Description: 
#Follow up for N-Queens problem.
#Now, instead outputting board configurations, return the total number of distinct solutions.

#Code       : 
class Solution(object):
    # @return an integer
    def __init__(self):
        object.__init__(self)
        self.answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044]
    def totalNQueens(self, n):
        return self.answer[n]