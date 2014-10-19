#Author     : sakura_kyon@hotmail.com
#Question   : Length of Last Word
#Link       : https://oj.leetcode.com/problems/length-of-last-word/
#Language   : python
#Status     : Accepted
#Run Time   : 116 ms
#Description: 
#Given a string s consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.
#If the last word does not exist, return 0.
####Note:### A word is defined as a character sequence consists of non-space characters only.
#For example, 
#Given s = `"Hello World"`,
#return `5`.

#Code       : 
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        p = re.compile('\w+')
        lst = p.findall(s)
        if lst:
            return len(lst[-1])
        else:
            return 0