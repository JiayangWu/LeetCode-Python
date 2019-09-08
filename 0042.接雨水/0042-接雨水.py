class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [0] + height + [0]
        left_max = [0 for _ in height]
        right_max = [0 for _ in height]
        
        
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])
            
        for i in range(len(height) - 2, -1, -1):
            # print i
            right_max[i] = max(height[i], right_max[i + 1])
        # print left_max, right_max     
        # res = [0 for _ in height]
        res = 0
        for i in range(1, len(height) - 2):
            res += min(left_max[i], right_max[i]) - height[i]
            
        return res