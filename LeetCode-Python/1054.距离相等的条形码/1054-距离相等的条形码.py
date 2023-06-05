class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        import heapq
        d = Counter(barcodes)
        res = []
        t = []
        for val, freq in d.items():
            t.append((-freq, val))
        heapify(t)

        last_pair = None
        while t:
            pair = heappop(t)
            val, freq = pair[1], -pair[0]
            res.append(val)
            if last_pair:
                heappush(t, last_pair)
            freq -= 1
            if freq:
                last_pair = (-freq, val)
            else:
                last_pair = None

        return res
