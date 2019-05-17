class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
 
        if not matrix or not matrix[0]:
            return list()
        m, n = len(matrix), len(matrix[0])
        
        po = [[0 for i  in range(n)] for j in range(m)] #po[i][j] = 1就代表matrix[i][j]可以被太平洋的水流到
        ao = [[0 for i  in range(n)] for j in range(m)] #同上，换成大西洋
        
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x0, y0, string):
            if visited[x0][y0] == 1:#来过了
                return     
            visited[x0][y0] = 1
            
            if string == "po":
                po[x0][y0] = 1
            else:
                ao[x0][y0] = 1
                
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0<= x < m and 0 <= y < n and matrix[x][y] >= matrix[x0][y0]: #可以流到下一个点
                    dfs(x, y, string)
            
        visited = [[0 for i in range(n)]  for j in range(m)]
        i = 0
        for j in range(n):
            dfs(i, j, "po") #上面的太平洋
            
        visited = [[0 for i in range(n)]  for j in range(m)]    
        i = m - 1
        for j in range(n):
            dfs(i, j, "ao") #下面的大西洋
            
        visited = [[0 for i in range(n)]  for j in range(m)]        
        j = 0
        for i in range(m):
            dfs(i, j, "po") #左边的太平洋
            
        visited = [[0 for i in range(n)]  for j in range(m)]    
        j = n - 1
        for i in range(m):
            dfs(i, j, "ao") #右边的大西洋
            
        res = []
        for i in range(m):
            for j in range(n):
                if po[i][j] and ao[i][j]: #取交集
                    res.append([i, j])
                    
        return res