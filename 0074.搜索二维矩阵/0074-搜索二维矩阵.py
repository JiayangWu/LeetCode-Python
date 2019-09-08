class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        i, j = m - 1, 0
        while 1:
            if 0 <= i < m and 0 <= j < n:
                cur = matrix[i][j]
                if cur == target:
                    return True
                elif cur < target:
                    j += 1
                elif cur > target:
                    i -= 1
            else:
                return False