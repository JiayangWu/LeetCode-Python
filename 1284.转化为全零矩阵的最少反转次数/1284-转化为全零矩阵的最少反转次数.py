import numpy
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        def check(matrix):

            return sum(sum(matrix, [])) == 0

        def encode(matrix):
            s = ""
            for row in matrix:
                for ch in row:
                    s += str(ch)
            return s 

        def decode(s):
            mat = []
            for ch in s:
                mat.append(int(ch))

            res = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    res[i][j] = mat[i * n + j]
            return res

        def convert(mat, i, j, m, n):
            for k in range(5):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    mat[x][y] ^= 1
            return mat
            
        res = -1
        from collections import deque 
        queue = deque([encode(mat)])

        dx = [1, 0, 0, -1, 0]
        dy = [0, 1, -1, 0, 0]
        visited = set()
        visited.add(encode(mat))
        while queue:
            res += 1
            for _ in range(len(queue)):
                encoded_cur = queue.popleft()
                cur = decode(encoded_cur)

                if check(cur):
                    return res
                
                for i in range(m):
                    for j in range(n):
                        mat = convert(cur, i, j, m, n)
                        encoded_mat = encode(mat)
                        if encoded_mat not in visited:
                            queue.append(encoded_mat)
                            visited.add(encoded_mat)

                        mat = convert(cur, i, j, m, n)
            
        return -1



