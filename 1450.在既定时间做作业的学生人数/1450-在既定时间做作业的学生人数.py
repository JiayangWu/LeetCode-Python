class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        return sum([1 for i in range(len(startTime)) if startTime[i] <= queryTime <= endTime[i]])