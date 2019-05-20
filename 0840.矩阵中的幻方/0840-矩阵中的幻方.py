class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #以左上角为00 ，构建子矩阵
        # x 范围 0 ~ m - 2, y范围0 ~ n - 2
        m,n = len(grid), len(grid[0])
        
        if m < 3 or n < 3: # corner case
            return 0
        
        res = 0
        for x in range(0, m - 2):
            for y in range(0, n - 2):
                # print grid[x][y]
                tempmatrix = []
                tempmatrix.append(grid[x][y:y + 3])
                tempmatrix.append(grid[x + 1][y : y + 3])
                tempmatrix.append(grid[x + 2][y : y + 3])
                # print tempmatrix
                if self.check(tempmatrix):
                    res += 1
                    
        return res
    
    def check(self, ma):
        digit = [1 for i in range(0, 10)]
        for row in ma:
            for d in row:
                if d > 9:
                    return False
                # print d
                digit[d] -= 1
        
        # print digit
        for i in range(1, 10):
            if digit[i] != 0:
                return False
            
        s = sum(ma[0])
        # print s
        for i in range(1, 3):
            if sum(ma[i]) != s:
                return False
        # print "pass1"
        sdia = 0
        for i in range(0, 3):
            sdia +=ma[i][i]
        if sdia != s:
            return False
        # print "pass2"
        sdia -= ma[2][0] + ma[1][1] + ma[0][2]
        if sdia != 0:
            return False
        
        # print "passs3"
        for j in range(0, 3):
            sc = 0
            for i in range(0,3):
                sc += ma[i][j]
            if sc != s:
                return False
            
        return True