class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # set row zero
                    for zj in range(n):
                        if matrix[i][zj] != 0:
                            matrix[i][zj] = "ZERO"
                    for zi in range(m):
                        if matrix[zi][j] != 0:
                            matrix[zi][j] = "ZERO"

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "ZERO":
                    matrix[i][j] = 0
                    