from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            d = self.getDistance(0, 0, x, y)
            if len(max_heap) < k:
                heappush(max_heap, (-d, [x, y]))
            else:
                heappushpop(max_heap, (-d, [x, y]))
        return [p for _, p in max_heap]


    def getDistance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5