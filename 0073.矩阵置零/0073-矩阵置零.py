class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        l_m = [1] * m
        l_n = [1] * n
        for i in range(m):
            for j in range(n):
                # print matrix[i][j], i, j
                if matrix[i][j] == 0:
                    l_m[i] = 0
                    l_n[j] = 0
        # print l_m, l_n
        for i in range(m):
            for j in range(n):
                # print i,j
                if l_m[i] == 0 or l_n[j] == 0:
                        matrix[i][j] = 0
                # print matrix
