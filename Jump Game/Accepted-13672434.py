#Author     : sakura_kyon@hotmail.com
#Question   : Jump Game
#Link       : https://oj.leetcode.com/problems/jump-game/
#Language   : python
#Status     : Accepted
#Run Time   : 196 ms
#Description: 
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position. 
#Determine if you are able to reach the last index.
#For example:
#A = `[2,3,1,1,4]`, return `true`.
#A = `[3,2,1,0,4]`, return `false`.
#Show Tags
#ArrayGreedy

#Code       : 
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) == 0:
            return False
        elif len(A) == 1:
            return True
    
        max_index = 0
        max_reach = 0
        step = 0
        while max_reach < len(A) - 1:
            old_max_index = max_index
            max_index = max_reach
            for i in range(old_max_index, max_reach + 1):
                max_reach = max(max_reach, i + A[i])
                if max_reach >= len(A):
                    return True
            step += 1
            if max_reach <= max_index:
                return False
        return True