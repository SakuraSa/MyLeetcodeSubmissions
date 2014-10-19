#Author     : sakura_kyon@hotmail.com
#Question   : Merge Intervals
#Link       : https://oj.leetcode.com/problems/merge-intervals/
#Language   : python
#Status     : Accepted
#Run Time   : 400 ms
#Description: 
#Given a collection of intervals, merge all overlapping intervals.
#For example,
#Given `[1,3],[2,6],[8,10],[15,18]`,
#return `[1,6],[8,10],[15,18]`.

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
    def merge(self, intervals):
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
        