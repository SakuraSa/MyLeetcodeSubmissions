#Author     : sakura_kyon@hotmail.com
#Question   : Letter Combinations of a Phone Number
#Link       : https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
#Language   : python
#Status     : Accepted
#Run Time   : 128 ms
#Description: 
#Given a digit string, return all possible letter combinations that the number could represent.
#A mapping of digit to letters (just like on the telephone buttons) is given below.
#```
####Input:###Digit string "23"
####Output:### ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#```
####Note:###
#Although the above answer is in lexicographical order, your answer could be in any order you want.
#Show Tags
#BacktrackingString

#Code       : 
phone_key = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def letterCombinations(digits_reversed, buf, res):
    if digits_reversed:
        c = digits_reversed.pop()
        for p in phone_key[c]:
            buf.append(p)
            letterCombinations(digits_reversed, buf, res)
            buf.pop()
        digits_reversed.append(c)
    else:
        res.append(''.join(buf))
    return res


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        digits = list(reversed(digits))
        return letterCombinations(digits, list(), list())