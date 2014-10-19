#Author     : sakura_kyon@hotmail.com
#Question   : Reverse Integer
#Link       : https://oj.leetcode.com/problems/reverse-integer/
#Language   : python
#Status     : Accepted
#Run Time   : 316 ms
#Description: 
#Reverse digits of an integer.
####Example1:### x =  123, return  321
####Example2:### x = -123, return -321
#[click to show spoilers.](#)
####Have you thought about this?###
#Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
#Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).

#Code       : 
class Solution:
    # @return an integer
    def reverse(self, x):
        if x<0:
            return -self.r(-x)
        else:
            return self.r(x)
        
    def r(self, x):
        return int(str(x)[::-1])
        