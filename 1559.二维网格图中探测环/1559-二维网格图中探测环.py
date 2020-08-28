class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        ufs = UnionFindSet(grid)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                for next_i, next_j in [(i - 1, j), (i, j - 1)]:
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == grid[i][j]:
                        if ufs.find(i * n + j) == ufs.find(next_i * n + next_j):
                            return True
                        else:
                            ufs.union(i * n + j, next_i * n + next_j)                 
        return False
        
class UnionFindSet(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.roots = [-1 for i in range(m*n)]
        self.rank = [0 for i in range(m*n)]
        self.count = 0
        
        for i in range(m):
            for j in range(n):
                self.roots[i * n + j] = i * n + j
                self.count += 1
        
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
        