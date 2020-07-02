class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or not intervals[0]:
            return 0
        intervals.sort()
        from heapq import * 
        queue = []
        heappush(queue, intervals[0][1])
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start >= queue[0]:
                heappop(queue)
            heappush(queue, end)

        return len(queue)