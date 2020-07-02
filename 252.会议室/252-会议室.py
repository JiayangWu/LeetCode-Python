class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals or not intervals[0]:
            return True 

        intervals.sort(key = lambda x:x[0])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]

            if s < end:
                return False
            end = e
        return True