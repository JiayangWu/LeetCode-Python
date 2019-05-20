class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        x, y = m - 1, 0
        while(1):
            if x < 0 or x >= m or y <0 or y >= n:
                break
            val = matrix[x][y]
            if val == target:
                return True
            elif val > target:
                x -= 1
            elif val <target:
                y += 1
                
        return False
