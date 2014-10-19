#Author     : sakura_kyon@hotmail.com
#Question   : Insert Interval
#Link       : https://oj.leetcode.com/problems/insert-interval/
#Language   : python
#Status     : Accepted
#Run Time   : 348 ms
#Description: 
#Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#You may assume that the intervals were initially sorted according to their start times.
####Example 1:###
#Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9]`.
####Example 2:###
#Given `[1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9]` in as `[1,2],[3,10],[12,16]`.
#This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.

#Code       : 
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x.start, x.end))
        ret = list()
        for it in intervals:
            if ret:
                last = ret.pop()
                if it.start <= last.end:
                    if it.end > last.end:
                        last.end = it.end
                    ret.append(last)
                else:
                    ret.append(last)
                    ret.append(it)
            else:
                ret.append(it)
        return ret