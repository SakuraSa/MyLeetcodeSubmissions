#Author     : sakura_kyon@hotmail.com
#Question   : Search in Rotated Sorted Array
#Link       : https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
#Language   : python
#Status     : Accepted
#Run Time   : 168 ms
#Description: 
#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You may assume no duplicate exists in the array.
#Show Tags
#ArrayBinary Search

#Code       : 
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target, begin=0, end=None):
        end = (len(A) - 1) if end is None else end 
        if begin > end:
            return -1
        elif begin == end:
            return begin if A[begin] == target else -1
        if A[begin] < A[end]:
            if A[begin] <= target <= A[end]:
                mid = (begin + end) / 2
                if target <= A[mid]:
                    return self.search(A, target, begin, mid)
                else:
                    return self.search(A, target, mid + 1, end)
            else:
                return -1
        else:
            mid = (begin + end) / 2
            value = self.search(A, target, begin, mid)
            if value >= 0:
                return value
            return self.search(A, target, mid + 1, end)