#Author     : sakura_kyon@hotmail.com
#Question   : Plus One
#Link       : https://oj.leetcode.com/problems/plus-one/
#Language   : python
#Status     : Accepted
#Run Time   : 160 ms
#Description: 
#Given a non-negative number represented as an array of digits, plus one to the number.
#The digits are stored such that the most significant digit is at the head of the list.
#Show Tags
#ArrayMath

#Code       : 
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return list(int(i) for i in str(int("".join(map(str, digits))) + 1))