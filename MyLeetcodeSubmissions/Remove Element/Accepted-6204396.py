#Author     : sakura_kyon@hotmail.com
#Question   : Remove Element
#Link       : https://oj.leetcode.com/problems/remove-element/
#Language   : python
#Status     : Accepted
#Run Time   : 164 ms
#Description: 
#Given an array and a value, remove all instances of that value in place and return the new length.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#Code       : 
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l = len(A)
        while True:
            try:
                A.remove(elem)
                l -= 1
            except Exception, e:
                break
        return l