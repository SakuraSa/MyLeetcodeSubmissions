#Author     : sakura_kyon@hotmail.com
#Question   : Divide Two Integers
#Link       : https://oj.leetcode.com/problems/divide-two-integers/
#Language   : python
#Status     : Accepted
#Run Time   : 312 ms
#Description: 
#Divide two integers without using multiplication, division and mod operator.
#Show Tags
#MathBinary Search

#Code       : 
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        value = operator.div(abs(dividend), abs(divisor))
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        return value * sign