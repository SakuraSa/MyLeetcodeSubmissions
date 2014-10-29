#Author     : sakura_kyon@hotmail.com
#Question   : Minimum Path Sum
#Link       : https://oj.leetcode.com/problems/minimum-path-sum/
#Language   : python
#Status     : Accepted
#Run Time   : 568 ms
#Description: 
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
####Note:### You can only move either down or right at any point in time.
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid[0]) - 1
        n = len(grid) - 1
        mem = {(0, 0): grid[0][0]}
        target_pos = (m, n)
        stack = [target_pos]
        while stack:
            x, y = pos = stack.pop()
            if pos in mem:
                continue
            left = down = 10000000000
            if x > 0:
                new_pos = (x - 1, y)
                if new_pos in mem:
                    left = mem[new_pos]
                else:
                    stack.append(pos)
                    stack.append(new_pos)
                    continue
            if y > 0:
                new_pos = (x, y - 1)
                if new_pos in mem:
                    down = mem[new_pos]
                else:
                    stack.append(pos)
                    stack.append(new_pos)
                    continue
            mem[pos] = min(left, down) + grid[y][x]
        return mem[target_pos]