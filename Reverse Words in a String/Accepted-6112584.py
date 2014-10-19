#Author     : sakura_kyon@hotmail.com
#Question   : Reverse Words in a String
#Link       : https://oj.leetcode.com/problems/reverse-words-in-a-string/
#Language   : python
#Status     : Accepted
#Run Time   : 120 ms
#Description: 
#Given an input string, reverse the string word by word.
#For example,
#Given s = "`the sky is blue`",
#return "`blue is sky the`".
#[click to show clarification.](#)
####Clarification:###
#* What constitutes a word?
#A sequence of non-space characters constitutes a word.
#* Could the input string contain leading or trailing spaces?
#Yes. However, your reversed string should not contain leading or trailing spaces.
#* How about multiple spaces between two words?
#Reduce them to a single space in the reversed string.

#Code       : 
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join([i for i in s.split(" ")[::-1] if i])