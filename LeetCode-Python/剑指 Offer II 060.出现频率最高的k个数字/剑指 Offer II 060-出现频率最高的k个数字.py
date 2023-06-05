from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        c = Counter(nums)
        # return sorted(set(nums), key = lambda x: -c[x])[:k]
        heap_set = set()
        min_heap = []
        for num in nums:
            if num not in heap_set:
                heap_set.add(num)
                if len(min_heap) < k:
                    heappush(min_heap, (c[num], num))
                else:
                    heappushpop(min_heap, (c[num], num))
        # print(min_heap)
        res = []
        while min_heap:
            res.append(heappop(min_heap)[1])
        return res
