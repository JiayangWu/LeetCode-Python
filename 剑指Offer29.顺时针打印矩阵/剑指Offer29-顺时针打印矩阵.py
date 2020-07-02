class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        
        x, y = 0, 0
        state = "r"
        cnt = 0
        res = []
        visited = set()
        while cnt < m * n:
            res.append(matrix[x][y])
            visited.add((x, y))
            if state == "r":
                if y + 1 < n and (x, y + 1) not in visited:
                    y += 1
                else:
                    x += 1
                    state = "d"
            elif state == "d":
                if x + 1 < m and (x + 1, y) not in visited:
                    x += 1
                else:
                    y -= 1
                    state = "l"
            elif state == "l":
                if y - 1 >= 0 and (x, y - 1) not in visited:
                    y -= 1
                else:
                    x -= 1
                    state = "u"
            elif state == "u":
                if x - 1 >= 0 and (x - 1, y) not in visited:
                    x -= 1
                else:
                    y += 1
                    state = "r"
            cnt += 1
        return res
                