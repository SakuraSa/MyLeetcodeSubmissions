#Author     : sakura_kyon@hotmail.com
#Question   : Roman to Integer
#Link       : https://oj.leetcode.com/problems/roman-to-integer/
#Language   : python
#Status     : Accepted
#Run Time   : 620 ms
#Description: 
#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.
#Show Tags
#MathString

#Code       : 
class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_ixc = {'I':5, 'X':50, 'C':500}
        value = 0
        for i in reversed(s):
            if i in roman_ixc and value >= roman_ixc[i]:
                value -= roman_dict[i]
            else:
                value += roman_dict[i]
        return value