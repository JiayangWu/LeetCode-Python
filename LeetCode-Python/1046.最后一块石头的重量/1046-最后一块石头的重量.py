from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heappush(max_heap, -stone)

        while len(max_heap) > 1:
            x, y = -heappop(max_heap), -heappop(max_heap)

            if y == x:
                continue
            else:
                heappush(max_heap, -(x - y))
        return -max_heap[0] if max_heap else 0