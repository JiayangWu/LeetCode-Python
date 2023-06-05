class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        state = "right"
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        count = m * n
        x, y = 0, 0
        res = []
        visited = set()
        while count:
            res.append(matrix[x][y])
            visited.add((x, y))
            if state == "right":
                if y + 1 < n and (x, y + 1) not in visited:
                    y += 1
                else:
                    state = "down"
                    x += 1
            elif state == "left":
                if y - 1 >= 0 and (x, y - 1) not in visited:
                    y -= 1
                else:
                    state = "up"
                    x -= 1
            elif state == "up":
                if x - 1 >= 0 and (x - 1, y) not in visited:
                    x -= 1
                else:
                    state = "right"
                    y += 1
            elif state == "down":
                if x + 1 < m and (x + 1, y) not in visited:
                    x += 1
                else:
                    state = "left"
                    y -= 1
            count -= 1
        return res