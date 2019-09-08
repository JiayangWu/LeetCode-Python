class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        state = "right"
        cnt = 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        while(cnt < n * n):
            cnt += 1
            res[i][j] = cnt
            if state == "right":
                j += 1
                if j == n or res[i][j] != 0:
                    i += 1
                    j -= 1
                    state = "down"
            elif state == "down":
                i += 1
                if i == n or res[i][j] != 0:
                    i -= 1
                    j -= 1
                    state = "left"
            elif state == "left":
                j -= 1
                if j == -1 or res[i][j] != 0:
                    j += 1
                    i -= 1
                    state = "up"
            elif state == "up":
                i -= 1
                if i == -1 or res[i][j] != 0:
                    i += 1
                    j += 1
                    state = "right"
        return res