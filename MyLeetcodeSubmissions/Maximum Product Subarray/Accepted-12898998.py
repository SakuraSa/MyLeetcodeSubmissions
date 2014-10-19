#Author     : sakura_kyon@hotmail.com
#Question   : Maximum Product Subarray
#Link       : https://oj.leetcode.com/problems/maximum-product-subarray/
#Language   : python
#Status     : Accepted
#Run Time   : 232 ms
#Description: 
#Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#For example, given the array `[2,3,-2,4]`,
#the contiguous subarray `[2,3]` has the largest product = `6`.

#Code       : 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        p1, p2, n, m = 1, 1, 0, A[0]
        for i in A:
            if i == 0:
                p1, n, m = 1, 0, max(m, 0)
            else:
                p1 *= i
                m = max(m, p1)
                if(n):
                    p2 *= i
                    m = max(m, p2)
                if(i < 0 and not n):
                    p2, n = 1, 1
        return m