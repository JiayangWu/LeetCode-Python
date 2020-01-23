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
            start, end = i - ranges[i], i + ranges[i]
            end = min(end, n + 1)
            start = max(start, 0)

            for j in range(start, end):
                reach[j] = max(end, reach[j])

        res = 0
        pos = 0
        while pos < n:
            if reach[pos] <= pos:
                return -1
            pos = reach[pos]
            res += 1
        return res
            