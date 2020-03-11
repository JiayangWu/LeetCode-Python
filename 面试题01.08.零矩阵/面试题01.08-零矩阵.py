class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix 

        m, n = len(matrix), len(matrix[0])

        row0, col0 = set(), set()

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row0.add(i)
                    col0.add(j)

        for i in range(m):
            for j in range(n):
                if i in row0 or j in col0:
                    matrix[i][j] = 0

        return matrix