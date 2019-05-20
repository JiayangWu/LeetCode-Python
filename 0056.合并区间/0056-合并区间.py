# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals,key=lambda x:x.start)
        res = []
        left = intervals[0].start
        right = intervals[0].end
        for item in intervals:
            if item.start <= right:
                right = max(right, item.end)
            else:
                res.append([left, right])
                left = item.start
                right = item.end
        res.append([left, right])
                
        return res
            