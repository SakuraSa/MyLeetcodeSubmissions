#Author     : sakura_kyon@hotmail.com
#Question   : Single Number II
#Link       : https://oj.leetcode.com/problems/single-number-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 252 ms
#Description: 
#Given an array of integers, every element appears three times except for one. Find that single one.
####Note:###
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Code       : 
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = dict()
        for i in A:
            d[i] = d.get(i, 0) + 1
        for k in d:
            if d[k] != 3:
                return k
        return "error"