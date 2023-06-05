class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for t in range(m):#ͬһ��
                        if matrix[t][j] != 0:
                            matrix[t][j] = "0"
                    for t in range(n):#ͬһ��
                        if matrix[i][t] != 0:
                            matrix[i][t] = "0"            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
        