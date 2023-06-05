from heapq import *
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = [-a for a in amount if a]
        heapify(max_heap)
        res = 0
        while len(max_heap) > 1:
            first, second = -heappop(max_heap), -heappop(max_heap)
            if first > 1:
                heappush(max_heap, -(first - 1))
            if second > 1:
                heappush(max_heap, -(second - 1))
            res += 1
        
        return res + -max_heap[0] if max_heap else res
        