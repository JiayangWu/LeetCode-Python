class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(0,len(M)):
            for j in range(0,len(M)):
                if i == j:
                    continue
                if M[i][j] == 1:
                    M[i][j] = 9
                    M[j][i] = 9
                    if M[i][i] != 0:
                        res += 1

                        M[i][i] = 0
                    self.loop(M, j)
                    
        for i in range(0, len(M)):
            alone = 1
            for j in range(0, len(M)):
                if M[i][j] == 9:
                    alone = 0
                    break
            res += alone
                
        return res
    def loop(self, M, x):
        for j in range(0, len(M)):
            if j == x:
                continue
            if M[x][j] == 1:
                M[x][j] = 9
                M[j][x] = 9
                self.loop(M, j)