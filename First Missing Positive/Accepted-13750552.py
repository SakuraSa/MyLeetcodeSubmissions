#Author     : sakura_kyon@hotmail.com
#Question   : First Missing Positive
#Link       : https://oj.leetcode.com/problems/first-missing-positive/
#Language   : python
#Status     : Accepted
#Run Time   : 188 ms
#Description: 
#Given an unsorted integer array, find the first missing positive integer.
#For example,
#Given `[1,2,0]` return `3`,
#and `[3,4,-1,1]` return `2`.
#Your algorithm should run in O(n) time and uses constant space.
#Show Tags
#Array

#Code       : 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        s = set(A)
        for i in range(1, len(s) + 1):
            if not i in s:
                return i
        return max(A) + 1