class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return []
        self.res = 0
        def dfs(start, tmp):  
            if start == n:
                self.res += 1
                return
            for i in range(n):
                tmp.append("." * i + "Q" + "." * (n - i - 1))
                if self.isValid(tmp, start, i,  n):
                    dfs(start + 1, tmp)
                tmp.pop()
        dfs(0, [])
        return self.res
    
    def isValid(self, tmp, x0, y0, n):
        self.add = x0 + y0
        self.sub = y0 - x0
        
        for i in range(len(tmp)): #ÅÐ¶ÏÁÐ
            if i == x0:
                continue
            if tmp[i][y0] == "Q":
                return False
            
        for i in range(min(n, len(tmp))): #ÅÐ¶Ï\
            if i == x0:
                continue
            # print i, j
            j = self.add - i
            # print i, j, self.add, tmp
            if 0 <= j < n and tmp[i][j] == "Q":
                return False
            j = i + self.sub
            if 0 <= j < n and tmp[i][j] == "Q":
                return False
        return True