#Author     : sakura_kyon@hotmail.com
#Question   : Single Number
#Link       : https://oj.leetcode.com/problems/single-number/
#Language   : python
#Status     : Accepted
#Run Time   : 316 ms
#Description: 
#Given an array of integers, every element appears twice except for one. Find that single one.
####Note:###
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Code       : 
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic=dict()
        for i in A:
            dic[i] = dic.get(i, 0) + 1
        for k in dic:
            if dic[k] == 1:
                return k