class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque
        queue = deque([(points[0][0], points[0][0] - points[0][1])])
        res = float("-inf")
        for yi, yj in points[1:]:
            while queue and queue[0][0] < yi - k:
                queue.popleft()
            if queue:
                res = max(res, -queue[0][1] + yi + yj)
            sub = yi - yj
            while queue and queue[-1][1] > sub:
                queue.pop()
            queue.append((yi, sub))
        return res