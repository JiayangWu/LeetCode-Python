class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:    
        import heapq
        min_heap = [1] # find the smallest ugly number
        visited = set()
        cnt = n
        while cnt:
            cur = heappop(min_heap)
            cnt -= 1
            if not cnt:
                return cur
            for multiple in primes:
                nxt = cur * multiple
                if nxt not in visited:
                    visited.add(nxt)
                    heappush(min_heap, nxt)