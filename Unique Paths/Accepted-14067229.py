#Author     : sakura_kyon@hotmail.com
#Question   : Unique Paths
#Link       : https://oj.leetcode.com/problems/unique-paths/
#Language   : python
#Status     : Accepted
#Run Time   : 196 ms
#Description: 
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?
#Above is a 3 x 7 grid. How many possible unique paths are there?
####Note:### m and n will be at most 100.
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        mem = {(1, 1): 1}
        target_pos = (m, n)
        stack = [target_pos]
        while stack:
            x, y = pos = stack.pop()
            if pos in mem:
                continue
            left = down = 0
            if x > 1:
                new_pos = (x - 1, y)
                if new_pos in mem:
                    left = mem[new_pos]
                else:
                    stack.append(pos)
                    stack.append(new_pos)
                    continue
            if y > 1:
                new_pos = (x, y - 1)
                if new_pos in mem:
                    down = mem[new_pos]
                else:
                    stack.append(pos)
                    stack.append(new_pos)
                    continue
            mem[pos] = left + down
        return mem[target_pos]
                
        