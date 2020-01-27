class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return None
        m, n = len(mat), len(mat[0])
        for j in range(n):
            i, l, pos = 0, [], []
            while i < m and j < n:
                l.append(mat[i][j])
                pos.append([i, j])
                i += 1
                j += 1
            l.sort()
            for i, p in enumerate(pos):
                x, y = p
                mat[x][y] = l[i]
        
        for i in range(1, m):
            j, l, pos = 0, [], []
            while i < m and j < n:
                l.append(mat[i][j])
                pos.append([i, j])
                i += 1
                j += 1
            l.sort()
            for i, p in enumerate(pos):
                x, y = p
                mat[x][y] = l[i]
        return mat