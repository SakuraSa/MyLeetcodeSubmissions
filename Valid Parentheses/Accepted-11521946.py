#Author     : sakura_kyon@hotmail.com
#Question   : Valid Parentheses
#Link       : https://oj.leetcode.com/problems/valid-parentheses/
#Language   : python
#Status     : Accepted
#Run Time   : 144 ms
#Description: 
#Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
#The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.

#Code       : 
opener = [')', '}', ']']
closer = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    # @return a boolean
    def isValid(self, s):
        st = list()
        lst = list(s)
        while lst:
            c = lst.pop()
            if c in opener:
                st.append(c)
            else:
                if not (st and closer[st.pop()] == c):
                    return False
        return not lst and not st