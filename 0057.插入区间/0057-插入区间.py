class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        return self.merge(intervals)
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        
        res = []
        for i, interval in enumerate(intervals):
            if interval[0] > end:
                res.append([start, end])
                start, end = interval[0], interval[1]
            else:
                end = max(end, interval[1])
        res.append([start, end])
        return res