#Author     : sakura_kyon@hotmail.com
#Question   : 3Sum Closest
#Link       : https://oj.leetcode.com/problems/3sum-closest/
#Language   : python
#Status     : Accepted
#Run Time   : 532 ms
#Description: 
#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#```
#    For example, given array S = {-1 2 1 -4}, and target = 1.
#    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#```
#Show Tags
#ArrayTwo Pointers

#Code       : 
class Solution:
    def threeSumClosest(self, num, target):
        n = len(num)
        num.sort()

        if n <= 3:
            return sum(num)

        ans = num[0] + num[1] + num[2]
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                count = num[i] + num[j] + num[k]
                if (abs(target - ans) > abs(target - count)):
                    ans = count
                    if ans == target:
                        return ans
                if count > target:
                    k -= 1
                else:
                    j += 1

        return ans