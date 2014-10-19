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
        p1, p2 = 1, 1
        nn = 0
        m = A[0]
        for i in A:
            if i == 0:
                p1, nn = 1, 0
                m = max(m, 0)
            else:
                p1 *= i
                m = max(m, p1)
                if(nn):
                    p2 *= i
                    m = max(m, p2)
                if(i < 0 and not nn):
                    p2, nn = 1, 1
        return m