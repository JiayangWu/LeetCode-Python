class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        dic = {}
        for i, (start, end) in enumerate(intervals):
            dic[start] = i

        res = [-1 for _ in range(len(intervals))]

        l = [interval[0] for interval in intervals]
        l = sorted(l, key = lambda x:x)

        for i, (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(l, end)
            if idx < len(l):
                res[i] = dic[l[idx]]
                
        return res
            
            