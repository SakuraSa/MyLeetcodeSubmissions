#Author     : sakura_kyon@hotmail.com
#Question   : Longest Consecutive Sequence
#Link       : https://oj.leetcode.com/problems/longest-consecutive-sequence/
#Language   : python
#Status     : Accepted
#Run Time   : 188 ms
#Description: 
#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#For example,
#Given `[100, 4, 200, 1, 3, 2]`,
#The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.
#Your algorithm should run in O(n) complexity.
#Show Tags
#Array

#Code       : 
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        max_length = 0
        now_length = 0
        last_num = None
        for n in sorted(num):
            if last_num == n:
                continue
            elif last_num == n - 1:
                now_length += 1
            else:
                now_length = 1
            last_num = n
            max_length = max(max_length, now_length)
        return max_length
                