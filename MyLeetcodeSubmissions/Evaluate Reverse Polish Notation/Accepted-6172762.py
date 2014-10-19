#Author     : sakura_kyon@hotmail.com
#Question   : Evaluate Reverse Polish Notation
#Link       : https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
#Language   : python
#Status     : Accepted
#Run Time   : 172 ms
#Description: 
#Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).
#Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.
#Some examples:
#```
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#```

#Code       : 
def div(a, b):
  res = abs(a) / abs(b)
  if (a < 0) ^ (b < 0):
    res *= -1
  return res 

class Solution:
    # @param tokens, a list of string
    # @return an integer
    ops = {"+":lambda a,b:a+b,
           "-":lambda a,b:a-b,
           "*":lambda a,b:a*b,
           "/":lambda a,b:div(a, b)}
    def evalRPN(self, tokens):
        obj = tokens.pop()
        if not obj in self.ops:
            return int(obj)
        a = self.evalRPN(tokens)
        b = self.evalRPN(tokens)
        res = self.ops[obj](b, a)
        return res
        