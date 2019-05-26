class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = sorted(heights)
        # print h
        res = 0
        for i in range(len(heights)):
            if h[i] != heights[i]:
                res += 1
        return res
            