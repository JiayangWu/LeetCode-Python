# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # tmp = Interval(newInterval[0], newInterval[1])
        intervals.append(newInterval)
        # intervals[-1] = newInterval
        # print type(intervals[0]), type(tmp)
        return self.merge(intervals)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if not intervals:
            return []
        intervals = sorted(intervals,key=lambda x:x[0])
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for item in intervals:
            if item[0] <= right:
                right = max(right, item[1])
            else:
                res.append([left, right])
                left = item[0]
                right = item[1]
        res.append([left, right])
                
        return res
            