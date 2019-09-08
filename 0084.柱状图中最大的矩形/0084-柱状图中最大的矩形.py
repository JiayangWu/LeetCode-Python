class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                    top = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * heights[top])
            stack.append(i)
        return res