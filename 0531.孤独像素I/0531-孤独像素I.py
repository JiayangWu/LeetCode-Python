class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        res = 0
        
        def check(x0, y0):      
            for x in range(0, m):  #同一列
                if picture[x][y0] == "B" and x != x0:
                    return False
            for y in range(0, n): #同一行
                if picture[x0][y] == "B" and y != y0:
                    return False
            return True
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and check(i, j):
                    res += 1
        return res