#Author     : sakura_kyon@hotmail.com
#Question   : 3Sum
#Link       : https://oj.leetcode.com/problems/3sum/
#Language   : python
#Status     : Accepted
#Run Time   : 576 ms
#Description: 
#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
####Note:###
#* Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#* The solution set must not contain duplicate triplets.
#```
#    For example, given array S = {-1 0 1 2 -1 -4},
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
#```
#Show Tags
#ArrayTwo Pointers

#Code       : 
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        s = set(num)
        ss = list()
        l = len(num)
        last_vi = None
        for i in range(l):
            vi = num[i]
            if vi == last_vi:
                continue
            else:
                last_vi = vi
            last_vj = None
            for j in range(i + 1, l):
                vj = num[j]
                if vj == last_vj:
                    continue
                else:
                    last_vj = vj
                v = - vi - vj
                if v < vj:
                    break
                if not v in s:
                    continue
                if v == vj and (j + 1 >= l or num[j + 1] != v):
                    continue
                ss.append([vi, vj, v])
        return ss