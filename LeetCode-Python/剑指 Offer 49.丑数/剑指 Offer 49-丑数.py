class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq

        min_heap = [1] # find the smallest ugly number
        visited = set()
        cnt = n
        while cnt:
            cur = heappop(min_heap)
            cnt -= 1
            if not cnt:
                return cur
            for multiple in [2, 3, 5]:
                nxt = cur * multiple
                if nxt not in visited:
                    visited.add(nxt)
                    heappush(min_heap, nxt)