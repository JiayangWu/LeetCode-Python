class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min1, min2 = m, n
        for op in ops:
            min1 = min(min1, op[0])
            min2 = min(min2, op[1])
        return min1 * min2