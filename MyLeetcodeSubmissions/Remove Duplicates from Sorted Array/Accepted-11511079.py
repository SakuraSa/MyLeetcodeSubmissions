#Author     : sakura_kyon@hotmail.com
#Question   : Remove Duplicates from Sorted Array
#Link       : https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
#Language   : python
#Status     : Accepted
#Run Time   : 368 ms
#Description: 
#Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.
#For example,
#Given input array A = `[1,1,2]`,
#Your function should return length = `2`, and A is now `[1,2]`.

#Code       : 
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        s = sorted(set(A))
        for i, value in enumerate(s):
            A[i] = value
        return len(s)
                