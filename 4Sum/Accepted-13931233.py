#Author     : sakura_kyon@hotmail.com
#Question   : 4Sum
#Link       : https://oj.leetcode.com/problems/4sum/
#Language   : python
#Status     : Accepted
#Run Time   : 664 ms
#Description: 
#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
####Note:###
#* Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
#* The solution set must not contain duplicate quadruplets.
#```
#    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#    A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)
#```
#Show Tags
#ArrayHash TableTwo Pointers

#Code       : 
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4:
            return []
        num.sort()
        mem = dict()
        res = set()
        l = len(num)
        for i in range(l):
            for j in range(i + 1, l):
                vi, vj = num[i], num[j]
                vs = vi + vj
                if not vs in mem:
                    mem[vs] = [(i, j)]
                else:
                    mem[vs].append((i, j))
        for i in range(l):
            for j in range(i + 1, l - 2):
                vi, vj = num[i], num[j]
                vs = vi + vj
                t = target - vs
                if t in mem:
                    for k in mem[t]:
                        if k[0] > j:
                            res.add((vi, vj, num[k[0]], num[k[1]]))
        return map(list, res)