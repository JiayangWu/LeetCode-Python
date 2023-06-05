from heapq import *
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_heap = [-a, -b, -c]
        heapify(max_heap)
        res = 0
        while len(max_heap) > 1:
            first, second = -heappop(max_heap), -heappop(max_heap)
            res += 1

            if first > 1:
                heappush(max_heap, -(first - 1))
            if second > 1:
                heappush(max_heap, -(second - 1))
        return res
