class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        from heapq import *
        if not arr or not arr[0]:
            return 0
        
        m, n = len(arr), len(arr[0])

        for i in range(1, m):
            max_heap = []
            for j in range(n):
                if len(max_heap) < 2:
                    heappush(max_heap, -arr[i - 1][j])
                else:
                    heappush(max_heap, -arr[i - 1][j])
                    heappop(max_heap)
            # print max_heap
            for j in range(n):
                arr[i][j] -= max_heap[1] if -max_heap[1] != arr[i - 1][j] else max_heap[0]
        return min(arr[-1])