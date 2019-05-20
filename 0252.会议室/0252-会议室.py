class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intvs = sorted(intervals, key = lambda x: x[0])
        for idx in range(1, len(intvs)):
            if intvs[idx][0] < intvs[idx - 1][1]:
                return False
        return True