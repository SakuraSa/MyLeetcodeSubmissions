#Author     : sakura_kyon@hotmail.com
#Question   : Regular Expression Matching
#Link       : https://oj.leetcode.com/problems/regular-expression-matching/
#Language   : python
#Status     : Accepted
#Run Time   : 352 ms
#Description: 
#Implement regular expression matching with support for `'.'` and `'*'`.
#```
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the ###entire### input string (not partial).
#The function prototype should be:
#bool isMatch(const char *s, const char *p)
#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "a*") → true
#isMatch("aa", ".*") → true
#isMatch("ab", ".*") → true
#isMatch("aab", "c*a*b") → true
#```

#Code       : 
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        return bool(re.match("^%s$" % p, s))