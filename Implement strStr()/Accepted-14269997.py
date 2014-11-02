#Author     : sakura_kyon@hotmail.com
#Question   : Implement strStr()
#Link       : https://oj.leetcode.com/problems/implement-strstr/
#Language   : python
#Status     : Accepted
#Run Time   : 180 ms
#Description: 
#Implement strStr().
#Returns a pointer to the first occurrence of needle in haystack, or ###null### if needle is not part of haystack.
#Show Tags
#Two PointersString

#Code       : 
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        try:
            return haystack[haystack.index(needle)::]
        except ValueError:
            return None
        