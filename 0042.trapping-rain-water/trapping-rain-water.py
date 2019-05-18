class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = [0 for _ in height]
        right_max = [0 for _ in height]
        water = [0 for _ in height]
        
        for i in range(len(height)):
            if i - 1 >= 0:
                left_max[i] = max(left_max[i - 1], height[i])
            else:
                left_max[i] = height[i]
            
        for i in range(len(height) - 1, -1, -1):
            if i  < len(height) - 1:
                right_max[i] = max(right_max[i + 1], height[i])
            else:
                right_max[i] = height[i]
                
        for i in range(len(height)):
            tmp = min(left_max[i], right_max[i]) - height[i]
            if tmp > 0:
                water[i] = tmp
        # print height     
        # print water
        # print left_max
        # print right_max
        return sum(water)