class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i]
                
        return matrix