class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # timeSeries.sort()
        # res = [0] * 30000000
        # for i in range(len(timeSeries)):
        #     for j in range(duration):
        #         res[timeSeries[i] + j] = 1
        # return sum(res)
        # timeSeries.sort()
        res = 0
        l = len(timeSeries)
        for i in range(l - 1):
            if timeSeries[i] + duration <= timeSeries[i+1]:        
                res += duration
            else:
                res += timeSeries[i+1] - timeSeries[i]
                
        return res + duration if l else res