#Author     : sakura_kyon@hotmail.com
#Question   : Median of Two Sorted Arrays
#Link       : https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
#Language   : python
#Status     : Accepted
#Run Time   : 580 ms
#Description: 
#There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#Code       : 
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        nl = sorted(A + B)
        if len(nl) % 2 == 1:
            return nl[len(nl) / 2]
        else:
            return (nl[len(nl) / 2] + nl[len(nl) / 2 - 1]) / 2.0
        