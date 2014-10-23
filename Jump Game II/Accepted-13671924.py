#Author     : sakura_kyon@hotmail.com
#Question   : Jump Game II
#Link       : https://oj.leetcode.com/problems/jump-game-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 272 ms
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
    
        opened = collections.deque()
        opened_set = set([0])
        opened.append((0, 0))
        closed_set = set()
    
        while opened:
            index, step = opened.popleft()
            opened_set.remove(index)
            closed_set.add(index)
            for to_index in xrange(index + A[index], index - A[index] - 1, -1):
                if to_index >= len(A) or to_index == index:
                    continue
                if to_index < 0:
                    break
                if not to_index in opened_set and not to_index in closed_set:
                    if to_index == len(A) - 1:
                        return step + 1
                    opened_set.add(to_index)
                    opened.append((to_index, step + 1))
        return -1