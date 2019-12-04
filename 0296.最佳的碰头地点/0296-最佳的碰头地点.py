class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row.append(i)
                    col.append(j)
        meet_point = [self.findMedian(row), self.findMedian(col)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += abs(i - meet_point[0]) + abs(j - meet_point[1])
        return res
        
        
    def findMedian(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
