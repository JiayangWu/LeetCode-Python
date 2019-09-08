class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        state = "right"
        cnt = 0
        res = []
        while(cnt < m * n):
            cnt += 1
            res.append(matrix[i][j])
            matrix[i][j] = "X"
            if state == "right":
                j += 1
                if j == n or matrix[i][j] == "X":
                    i += 1
                    j -= 1
                    state = "down"
            elif state == "down":
                i += 1
                if i == m or matrix[i][j] == "X":
                    i -= 1
                    j -= 1
                    state = "left"
            elif state == "left":
                j -= 1
                if j == -1 or matrix[i][j] == "X":
                    j += 1
                    i -= 1
                    state = "up"
            elif state == "up":
                i -= 1
                if i == -1 or matrix[i][j] == "X":
                    i += 1
                    j += 1
                    state = "right"
        return res