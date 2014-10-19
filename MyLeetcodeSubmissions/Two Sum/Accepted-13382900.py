#Author     : sakura_kyon@hotmail.com
#Question   : Two Sum
#Link       : https://oj.leetcode.com/problems/two-sum/
#Language   : python
#Status     : Accepted
#Run Time   : 296 ms
#Description: 
#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution.
####Input:### numbers={2, 7, 11, 15}, target=9
####Output:### index1=1, index2=2

#Code       : 
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sorted_num = sorted([(n, i) for i, n in enumerate(num)])
        for in1 in range(len(sorted_num)):
            n1, i1 = sorted_num[in1]
            for in2 in range(in1 + 1, len(sorted_num)):
                n2, i2 = sorted_num[in2]
                s = n1 + n2
                if s == target:
                    return sorted([i1 + 1, i2 + 1])
                elif s > target:
                    break
        return "not found"