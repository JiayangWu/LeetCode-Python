class UnionFindSet(object):
    def __init__(self, grid):

        m, n = len(grid), len(grid[0])
        self.roots = [i for i in range(m * n)]
        self.rank = [0 for i in range(m * n)]
        self.count = n
        
        for i in range(m):
            for j in range(n):
                self.roots[i *n + j] = i * n +j

    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        for root in tmp:
            self.roots[root] = member
        return member
        
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x, y):
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
 
                if xx >= 0 and xx < m and yy >= 0 and yy < n: #当前坐标有效
                    if board[xx][yy] == "O":
                        board[xx][yy] = "P" #给走过的点染色
                        dfs(xx, yy)
        #--------以下在从四周往里找相邻的所有点
        i = 0
        for j in range(n): #上边
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j)
 
        i = m - 1
        for j in range(n): #下边
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j)    
        j = 0        
        for i in range(m): #左边
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j) 
 
        j = n - 1     
        for i in range(m): #右边
            if board[i][j] == "O":
                board[i][j] = "P"
                dfs(i, j) 
        #--------以上在从四周往里找相邻的所有点
        # print board
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "P": #统计一下还有多少个没有去过的点
                    
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                        
        return board
                        
                     