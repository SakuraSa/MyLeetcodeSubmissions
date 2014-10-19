#Author     : sakura_kyon@hotmail.com
#Question   : Valid Number
#Link       : https://oj.leetcode.com/problems/valid-number/
#Language   : python
#Status     : Accepted
#Run Time   : 384 ms
#Description: 
#Validate if a given string is numeric.
#Some examples:
#`"0"` => `true`
#`"   0.1  "` => `true`
#`"abc"` => `false`
#`"1 a"` => `false`
#`"2e10"` => `true`
####Note:### It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

#Code       : 
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        return bool( re.match("^(\+|-)?(\d+(\.\d*)?|\.\d+)(e(\+|-)?\d+)?$", s.strip()) )