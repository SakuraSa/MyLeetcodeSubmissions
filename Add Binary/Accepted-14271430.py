#Author     : sakura_kyon@hotmail.com
#Question   : Add Binary
#Link       : https://oj.leetcode.com/problems/add-binary/
#Language   : python
#Status     : Accepted
#Run Time   : 180 ms
#Description: 
#Given two binary strings, return their sum (also a binary string).
#For example,
#a = `"11"`
#b = `"1"`
#Return `"100"`.
#Show Tags
#MathString

#Code       : 
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        byte = 2
        add = 0
        res = []
        while a or b or add > 0:
            now = add
            if a:
                now += a.pop()
            if b:
                now += b.pop()
            add = now / byte
            res.append(now % byte)
        return "".join(map(str, reversed(res)))