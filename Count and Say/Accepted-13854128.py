#Author     : sakura_kyon@hotmail.com
#Question   : Count and Say
#Link       : https://oj.leetcode.com/problems/count-and-say/
#Language   : python
#Status     : Accepted
#Run Time   : 148 ms
#Description: 
#The count-and-say sequence is the sequence of integers beginning as follows:
#`1, 11, 21, 1211, 111221, ...`
#`1` is read off as `"one 1"` or `11`.
#`11` is read off as `"two 1s"` or `21`.
#`21` is read off as `"one 2`, then `one 1"` or `1211`.
#Given an integer n, generate the nth sequence.
#Note: The sequence of integers will be represented as a string.
#Show Tags
#String

#Code       : 
class Solution:
    # @return a string
    def countAndSay(self, n):
        buf = ['1']
        index = 1
        while index < n:
            index += 1
            new_buf = []
            v = buf[0]
            c = 0
            for e in buf:
                if v == e:
                    c += 1
                else:
                    new_buf.append(str(c))
                    new_buf.append(v)
                    v = e
                    c = 1
            new_buf.append(str(c))
            new_buf.append(v)
            buf = new_buf
        return ''.join(buf)