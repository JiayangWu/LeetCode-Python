class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        b = [[0 for _ in range(m)] for _ in range(n)]
        for row, col in indices:
            for i in range(m):
                b[row][i] += 1
                
            for j in range(n):
                b[j][col] += 1
        
        res = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] % 2:
                    res += 1
        return res