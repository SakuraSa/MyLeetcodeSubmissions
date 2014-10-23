#Author     : sakura_kyon@hotmail.com
#Question   : Jump Game II
#Link       : https://oj.leetcode.com/problems/jump-game-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 248 ms
#Description: 
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position. 
#Your goal is to reach the last index in the minimum number of jumps.
#For example:
#Given array A = `[2,3,1,1,4]`
#The minimum number of jumps to reach the last index is `2`. (Jump `1` step from index 0 to 1, then `3` steps to the last index.)
#Show Tags
#ArrayGreedy

#Code       : 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1:
            return 0
    
        max_index = 0
        max_reach = 0
        step = 0
        while max_reach < len(A) - 1:
            old_max_index = max_index
            max_index = max_reach
            for i in range(old_max_index, max_reach + 1):
                max_reach = max(max_reach, i + A[i])
                if max_reach >= len(A):
                    break
            step += 1
    
        return step