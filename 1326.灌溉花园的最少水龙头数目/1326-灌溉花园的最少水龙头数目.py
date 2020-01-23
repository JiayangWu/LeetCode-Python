class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        ivls = []
        reach = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            start, end = max(i - ranges[i], 0), min(i + ranges[i], n + 1)
            for j in range(start, end):
                reach[j] = max(end, reach[j])

        res = 0
        pos = 0
        while pos < n:
            if reach[pos] <= pos: # 无法继续抵达更远的位置
                return -1
            pos = reach[pos]
            res += 1
        return res