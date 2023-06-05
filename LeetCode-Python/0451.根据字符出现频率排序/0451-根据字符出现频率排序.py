from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)

        max_heap = []
        for char, freq in c.items():
            heappush(max_heap, (-freq, char))

        res = ""
        while max_heap:
            freq, char = heappop(max_heap)
            res += -freq * char
        return res