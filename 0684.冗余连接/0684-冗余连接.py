class UnionFindSet(object):
    def __init__(self, edges):

        # m, n = len(grid), len(grid[0])
        self.roots = [i for i in range(1001)]
        self.rank = [0 for i in range(1001)]
        self.count = 0
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     self.roots[i * n + j] = i * n + j
#                     self.count += 1
        
        
        
    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        # for root in tmp:
        #     self.roots[root] = member
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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ufs = UnionFindSet(edges)
        res = []
        for edge in edges:
            x, y = edge[0], edge[1]
            p, q = ufs.find(x), ufs.find(y)
            # print (x, y), (p, q)
            if p == q:
                res = edge
            else:          
                ufs.union(p, q)
        
        return res
        
    