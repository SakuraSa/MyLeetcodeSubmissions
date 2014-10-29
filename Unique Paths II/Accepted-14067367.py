#Author     : sakura_kyon@hotmail.com
#Question   : Unique Paths II
#Link       : https://oj.leetcode.com/problems/unique-paths-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 196 ms
#Description: 
#Follow up for "Unique Paths":
#Now consider if some obstacles are added to the grids. How many unique paths would there be?
#An obstacle and empty space is marked as `1` and `0` respectively in the grid.
#For example,
#There is one obstacle in the middle of a 3x3 grid as illustrated below.
#```
#[
#  [0,0,0],
#  [0,1,0],
#  [0,0,0]
#]
#```
#The total number of unique paths is `2`.
####Note:### m and n will be at most 100.
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid[0]) - 1
        n = len(obstacleGrid) - 1
        mem = {(0, 0): 1 if obstacleGrid[0][0] == 0 else 0}
        target_pos = (m, n)
        stack = [target_pos]
        while stack:
            x, y = pos = stack.pop()
            if pos in mem:
                continue
            elif obstacleGrid[y][x] == 1:
                mem[pos] = 0
                continue
            left = down = 0
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
            mem[pos] = left + down
        return mem[target_pos]