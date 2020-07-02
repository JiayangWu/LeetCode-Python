class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        return self.merge(intervals + [newInterval])



    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or not intervals[0]:
            return intervals
        
        intervals = sorted(intervals, key = lambda x:x[0])

        res = []
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals:
            s, e = interval[0], interval[1]
            
            if s <= end: # overlap
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e 

        res.append([start, end])
        return res