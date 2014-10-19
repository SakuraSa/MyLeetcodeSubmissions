#Author     : sakura_kyon@hotmail.com
#Question   : ZigZag Conversion
#Link       : https://oj.leetcode.com/problems/zigzag-conversion/
#Language   : python
#Status     : Accepted
#Run Time   : 428 ms
#Description: 
#The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#```
#P   A   H   N
#A P L S I I G
#Y   I   R
#```
#And then read line by line: `"PAHNAPLSIIGYIR"`
#Write the code that will take a string and make this conversion given a number of rows:
#```string convert(string text, int nRows);```
#`convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.

#Code       : 
def cv(s, nRows):
    if nRows <= 1 or len(s) == 0:
        yield s
        return
    slen = len(s)
    for i in range(min(slen, nRows)):
        index, k = i, 1
        yield s[i]
        while index < slen:
            if i == 0 or i == nRows - 1:
                index += 2 * nRows - 2
            elif k & 1:
                index += 2 * (nRows - 1 - i)
            else:
                index += 2 * i
            if index < slen:
                yield s[index]
            k += 1

class Solution:
    def convert(self, s, nRows):
        return "".join(cv(s, nRows))