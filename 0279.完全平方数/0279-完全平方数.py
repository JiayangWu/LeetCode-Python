class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import deque
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            cur, step = queue.popleft()
            for i in range(1, int(n ** 0.5) + 1):
                s = cur + i ** 2
                if s == n:
                    return step + 1
                if s not in visited:
                    visited.add(s)
                    queue.append((s, step + 1))
                