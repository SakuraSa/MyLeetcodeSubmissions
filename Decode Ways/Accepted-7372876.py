#Author     : sakura_kyon@hotmail.com
#Question   : Decode Ways
#Link       : https://oj.leetcode.com/problems/decode-ways/
#Language   : python
#Status     : Accepted
#Run Time   : 236 ms
#Description: 
#A message containing letters from `A-Z` is being encoded to numbers using the following mapping:
#```
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#```
#Given an encoded message containing digits, determine the total number of ways to decode it.
#For example,
#Given encoded message `"12"`,
#it could be decoded as `"AB"` (1 2) or `"L"` (12).
#The number of ways decoding `"12"` is 2.

#Code       : 
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        self.mem = {"": 0}
        return self.count(s)

    def count(self, s):
        if len(s) == 1:
            return int(self.get(s, 1))
        if s in self.mem:
            return self.mem[s]
        ret = 0
        for i in range(1, 3):
            if self.get(s, i):
                res = s[i::]
                if res:
                    ret += self.count(res)
                else:
                    ret += 1
        self.mem[s] = ret
        return ret

    def get(self, s, l):
        if l > len(s):
            return None
        else:
            return not(s.startswith('0')) and 1 <= int(s[0:l]) <= 26