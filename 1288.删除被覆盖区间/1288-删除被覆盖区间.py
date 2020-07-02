class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x:(x[0], x[1]))

        start, end = intervals[0][0], intervals[0][1]

        n = len(intervals)
        max_end = intervals[0][1]
        for s, e in intervals:
            if max_end >= e:
                n -= 1
            else:
                max_end = e 
        
        return n + 1