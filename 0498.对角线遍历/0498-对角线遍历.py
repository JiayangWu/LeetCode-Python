class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 向右上方走，x -= 1, y += 1
        # 向左下角走，x += 1, y -= 1
        m = len(matrix)
        if not m :
            return []
        n = len(matrix[0])
        if not n :
            return []

        cnt = 0
        x, y = 0, 0
        res = list()
        direction = "right"
        while(cnt < m * n):
            cnt += 1
            # print direction, x, y, matrix[x][y]
            res.append(matrix[x][y])
            if direction == "right":#向右上方走
                if x >= 1 and y < n - 1:
                    x -= 1
                    y += 1
                    continue
                else:
                    direction = "left" #调换方向
                    if x == 0 and y < n - 1: #碰上壁
                        y += 1
                    elif  y == n - 1: #碰右壁
                        x += 1
            else: # 向左下方走
                if x < m - 1 and y >= 1:
                    x += 1
                    y -= 1
                    continue
                else:
                    direction = "right" #调换方向
                    if x == m - 1: # 碰下壁
                        y += 1
                    elif y == 0 and x < m - 1: #碰左壁
                        x += 1 
            # print res
        return res
                        