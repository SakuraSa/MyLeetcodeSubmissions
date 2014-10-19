#Author     : sakura_kyon@hotmail.com
#Question   : Generate Parentheses
#Link       : https://oj.leetcode.com/problems/generate-parentheses/
#Language   : python
#Status     : Accepted
#Run Time   : 164 ms
#Description: 
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#For example, given n = 3, a solution set is:
#`"((()))", "(()())", "(())()", "()(())", "()()()"`

#Code       : 
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.answers = list()
        self.gp(n, 0, 0, list())
        return self.answers
    
    def gp(self, n, l, r, stack):
        if l == r == n:
            self.answers.append(''.join(stack))
            return
        if l < n:
            stack.append('(')
            self.gp(n, l + 1, r, stack)
            stack.pop()
        if r < l:
            stack.append(')')
            self.gp(n, l, r + 1, stack)
            stack.pop()
        