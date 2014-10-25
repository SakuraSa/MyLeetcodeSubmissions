#Author     : sakura_kyon@hotmail.com
#Question   : Maximum Subarray
#Link       : https://oj.leetcode.com/problems/maximum-subarray/
#Language   : python
#Status     : Accepted
#Run Time   : 280 ms
#Description: 
#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#For example, given the array `[&#8722;2,1,&#8722;3,4,&#8722;1,2,1,&#8722;5,4]`,
#the contiguous subarray `[4,&#8722;1,2,1]` has the largest sum = `6`.
#[click to show more practice.](#)
####More practice:###
#If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#Show Tags
#Divide and ConquerArrayDynamic Programming

#Code       : 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        l = []
        l.append(A[0])
        for i in range(1, len(A)):
            l.append(max(A[i], l[i - 1] + A[i]))
        return max(l)