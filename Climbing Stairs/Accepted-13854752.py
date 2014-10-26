#Author     : sakura_kyon@hotmail.com
#Question   : Climbing Stairs
#Link       : https://oj.leetcode.com/problems/climbing-stairs/
#Language   : python
#Status     : Accepted
#Run Time   : 104 ms
#Description: 
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Show Tags
#Dynamic Programming

#Code       : 
sqr5 = 5 ** .5
p1 = (1 + sqr5) / 2
p2 = 1 - p1
def fibonacci(n):
    return int(.5 + (p1 ** (n + 1) - p2 ** (n + 1)) / sqr5)

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        return fibonacci(n)