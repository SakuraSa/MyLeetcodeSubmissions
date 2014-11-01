#Author     : sakura_kyon@hotmail.com
#Question   : Pascal&#39;s Triangle II
#Link       : https://oj.leetcode.com/problems/pascals-triangle-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 152 ms
#Description: 
#Given an index k, return the kth row of the Pascal's triangle.
#For example, given k = 3,
#Return `[1,3,3,1]`.
####Note:###
#Could you optimize your algorithm to use only O(k) extra space?
#Show Tags
#Array

#Code       : 
def f(n):
    j = 1
    for c in xrange(n + 1):
        yield j
        j = j * (n - c) / (c + 1) 

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        return list(f(rowIndex))
        