#Author     : sakura_kyon@hotmail.com
#Question   : Wildcard Matching
#Link       : https://oj.leetcode.com/problems/wildcard-matching/
#Language   : python
#Status     : Accepted
#Run Time   : 464 ms
#Description: 
#Implement wildcard pattern matching with support for `'?'` and `'*'`.
#```
#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).
#The matching should cover the ###entire### input string (not partial).
#The function prototype should be:
#bool isMatch(const char *s, const char *p)
#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "*") → true
#isMatch("aa", "a*") → true
#isMatch("ab", "?*") → true
#isMatch("aab", "c*a*b") → false
#```
#Show Tags
#Dynamic ProgrammingBacktrackingGreedyString

#Code       : 
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        pt_s = 0
        pt_p = 0
        pt_star = None
        pt_ss = None
        while pt_s < len(s):
            pc = p[pt_p] if pt_p < len(p) else None
            sc = s[pt_s]
            if pc == "?" or pc == sc:
                pt_s += 1
                pt_p += 1
                continue
            elif pc == "*":
                pt_star = pt_p
                pt_p += 1
                pt_ss = pt_s
                continue
            elif not pt_star is None:
                pt_p = pt_star + 1
                pt_ss += 1
                pt_s = pt_ss
                continue
            return False
        while pt_p < len(p) and p[pt_p] == "*":
            pt_p += 1
        return (pt_s == len(s)) and (pt_p == len(p))
        