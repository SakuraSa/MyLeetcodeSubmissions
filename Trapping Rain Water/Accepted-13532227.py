#Author     : sakura_kyon@hotmail.com
#Question   : Trapping Rain Water
#Link       : https://oj.leetcode.com/problems/trapping-rain-water/
#Language   : python
#Status     : Accepted
#Run Time   : 272 ms
#Description: 
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 
#For example, 
#Given `[0,1,0,2,1,0,1,3,2,1,2,1]`, return `6`.
#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. ###Thanks Marcos### for contributing this image!
#Show Tags
#ArrayStackTwo Pointers

#Code       : 
def trap(heights):
    left_height = []
    max_height = 0
    for h in heights:
        max_height = max(max_height, h)
        left_height.append(max_height)
    right_height = []
    max_height = 0
    for h in heights[::-1]:
        max_height = max(max_height, h)
        right_height.append(max_height)
    right_height = right_height[::-1]
    s = 0
    for lh, h, rh in zip(left_height, heights, right_height):
        if lh > h and rh > h:
            s += min(lh, rh) - h
    return s

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        return trap(A)
        