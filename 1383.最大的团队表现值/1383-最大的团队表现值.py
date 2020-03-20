class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        combine = [(speed[i], efficiency[i]) for i in range(n)]
        combine = sorted(combine, key = lambda x: - x[1])
        res = 0
        MOD = 10 ** 9 + 7
        min_heap = []
        speed_sum = 0
        for i in range(n):
            s, e = combine[i]
            if len(min_heap) < k:
                heappush(min_heap, s)
                speed_sum += s
            else:
                if min_heap and min_heap[0] < s:
                    speed_sum = speed_sum - min_heap[0] + s
                    heappush(min_heap, s)
                    heappop(min_heap)
                    
            res = max(res, speed_sum * e)
        return res % MOD