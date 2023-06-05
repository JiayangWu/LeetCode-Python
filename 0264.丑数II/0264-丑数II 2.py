class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from heapq import *
        l = [1]
        heapify(l)
        cnt = 1
        used = set([1])
        while cnt < n:
            cur = heappop(l)
            if cur * 2 not in used:
                heappush(l, cur * 2)
                used.add(cur * 2)
            if cur * 3 not in used:
                heappush(l, cur * 3)
                used.add(cur * 3)
            if cur * 5 not in used:
                used.add(cur * 5)
                heappush(l, cur * 5)
            cnt += 1
        return heappop(l)