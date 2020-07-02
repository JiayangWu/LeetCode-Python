class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        res = 0
        while(lo < hi):
            if height[lo] > height[hi]:
                area = height[hi] * (hi - lo)
                hi -= 1
            else:
                area = height[lo] * (hi - lo)
                lo += 1
            # print area
            res = max(area, res)
            
        return res
                