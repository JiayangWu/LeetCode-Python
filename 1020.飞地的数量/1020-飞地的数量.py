class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        
        def dfs(x, y):
            dx = [0, 1, -1, 0]
            dy = [-1, 0, 0, + 1]
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]

                if xx >= 0 and xx < m and yy >= 0 and yy < n: #当前坐标有效
                    if A[xx][yy] == 1:
                        A[xx][yy] = 2 #给走过的点染色
                        dfs(xx, yy)
        #--------以下在从四周往里找相邻的所有点
        i = 0
        for j in range(n): #上边
            if A[i][j] == 1:
                A[i][j] = 2
                dfs(i, j)

        i = m - 1
        for j in range(n): #下边
            if A[i][j] == 1:
                A[i][j] = 2
                dfs(i, j)    
        j = 0        
        for i in range(m): #左边
            if A[i][j] == 1:
                A[i][j] = 2
                dfs(i, j) 

        j = n - 1     
        for i in range(m): #右边
            if A[i][j] == 1:
                A[i][j] = 2
                dfs(i, j) 
        #--------以上在从四周往里找相邻的所有点
        
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1: #统计一下还有多少个没有去过的点
                    res += 1
          
        return res