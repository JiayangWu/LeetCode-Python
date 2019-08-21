class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x: x[0])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            
            if end > start:
                return False
            end = intervals[i][1]
            
        return True