from heapq import *
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            heappush(max_heap, -gift)

        while k:
            gift = -heappop(max_heap)
            heappush(max_heap, -int(gift ** 0.5))
            k -= 1
        return -sum(max_heap)
