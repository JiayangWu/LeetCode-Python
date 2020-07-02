class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        x, y = m - 1, 0 
        while 0 <= x < m and 0 <= y < n:
            if matrix[x][y] == target:
                return True 
            elif matrix[x][y] > target:
                x -= 1 
            else: 
                y += 1
        return False