#Author     : sakura_kyon@hotmail.com
#Question   : Pascal&#39;s Triangle
#Link       : https://oj.leetcode.com/problems/pascals-triangle/
#Language   : python
#Status     : Accepted
#Run Time   : 128 ms
#Description: 
#Given numRows, generate the first numRows of Pascal's triangle.
#For example, given numRows = 5,
#Return
#```
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]
#```
#Show Tags
#Array

#Code       : 
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        for _ in xrange(numRows):
            if res:
                now = []
                left = 0
                for i in res[-1]:
                    now.append(left + i)
                    left = i
                now.append(1)
                res.append(now)
            else:
                res.append([1])
        return res