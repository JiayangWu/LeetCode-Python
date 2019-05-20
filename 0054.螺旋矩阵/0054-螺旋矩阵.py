class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        r, i, j, di, dj = list(), 0, 0, 0, 1
        
        for _ in range(m * n):
            r.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i + di) % m][(j + dj) % n] == None: #来过了改转向了
                di, dj = dj, -di #0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1                
            i += di
            j += dj

        return r
                    
                    
                
                        
                
                    
        