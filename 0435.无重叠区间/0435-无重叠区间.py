class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or not intervals[0]:
            return 0

        intervals = sorted(intervals, key = lambda x:x[1])
        pre_end = intervals[0][1]
        canAttendCnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= pre_end: # start later than previous one end
                canAttendCnt += 1
                pre_end = intervals[i][1]
        return len(intervals) - canAttendCnt

