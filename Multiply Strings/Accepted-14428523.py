#Author     : sakura_kyon@hotmail.com
#Question   : Multiply Strings
#Link       : https://oj.leetcode.com/problems/multiply-strings/
#Language   : python
#Status     : Accepted
#Run Time   : 192 ms
#Description: 
#Given two numbers represented as strings, return multiplication of the numbers as a string.
#Note: The numbers can be arbitrarily large and are non-negative.
#Show Tags
#MathString

#Code       : 
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(long(num1) * long(num2))