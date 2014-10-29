#Author     : sakura_kyon@hotmail.com
#Question   : Longest Common Prefix
#Link       : https://oj.leetcode.com/problems/longest-common-prefix/
#Language   : python
#Status     : Accepted
#Run Time   : 196 ms
#Description: 
#Write a function to find the longest common prefix string amongst an array of strings.
#Show Tags
#String

#Code       : 
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        perfix = list(strs[0])
        for s in strs:
            while perfix and len(perfix) > len(s):
                perfix.pop()
            index = len(s)
            for i in range(min(len(s), len(perfix))):
                if s[i] != perfix[i]:
                    index = i
                    break
            while perfix and len(perfix) > index:
                perfix.pop()
        return "".join(perfix)
            
        