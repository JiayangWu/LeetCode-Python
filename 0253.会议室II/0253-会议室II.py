class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x :x[1])
        record = [0 for _ in range(intervals[-1][1] + 2)]
        
        for i, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            record[start] += 1
            record[end] -= 1
        
        # print record
        for i in range(1, len(record)):
            record[i] += record[i - 1]
        
        return max(record)