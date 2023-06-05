class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_zero, col_zero = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    row_zero.add(i)
                    col_zero.add(j)

        for row_index in row_zero:
            matrix[row_index] = [0] * len(matrix[0])

        for col_index in col_zero:
            for i in range(len(matrix)):
                matrix[i][col_index] = 0


                