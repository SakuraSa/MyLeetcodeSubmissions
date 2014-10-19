#Author     : sakura_kyon@hotmail.com
#Question   : Valid Palindrome
#Link       : https://oj.leetcode.com/problems/valid-palindrome/
#Language   : python
#Status     : Accepted
#Run Time   : 284 ms
#Description: 
#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#For example,
#`"A man, a plan, a canal: Panama"` is a palindrome.
#`"race a car"` is not a palindrome.
####Note:###
#Have you consider that the string might be empty? This is a good question to ask during an interview.
#For the purpose of this problem, we define empty string as valid palindrome.

#Code       : 
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        x = re.findall("\d|\w", s.lower())
        return tuple(x) == tuple(x[::-1])
        