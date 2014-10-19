#Author     : sakura_kyon@hotmail.com
#Question   : Anagrams
#Link       : https://oj.leetcode.com/problems/anagrams/
#Language   : python
#Status     : Accepted
#Run Time   : 404 ms
#Description: 
#Given an array of strings, return all groups of strings that are anagrams.
#Note: All inputs will be in lower-case.

#Code       : 
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        counter = collections.Counter(tuple(sorted(s)) for s in strs)
        return filter(lambda x: counter[tuple(sorted(x))] > 1, strs)