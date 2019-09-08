class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        if not intervals[0]:
            return 1
        intervals = sorted(intervals, key = lambda x: x[1])
        record = [0 for _ in range(intervals[-1][1] + 1)]
        
        for interval in intervals:
            # print record
            begin, end = interval[0], interval[1]
            record[begin] += 1
            record[end] -= 1
            
        for i, x in enumerate(record):
            if i > 0:
                record[i] += record[i - 1]
        return max(record)