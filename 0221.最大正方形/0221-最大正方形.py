class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        self.res = 0
        
        def find(x, y):
            for length in range(1, min(m - i, n - j) + 1):#length «±ﬂ≥§
                cnt = 0
                
                for k in range(length):
                    for t in range(length):
                        xx = x + k
                        yy = y + t
                        
                        if 0 <= xx <m and 0 <= yy < n:
                            if matrix[xx][yy] == "0":
                                return 
                            else:
                                cnt += 1
                if cnt == length ** 2:
                    self.res = max(self.res, cnt)
                                 
                
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    find(i, j)
                    
        return self.res
                           