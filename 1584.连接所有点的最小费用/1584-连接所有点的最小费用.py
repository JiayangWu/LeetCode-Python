
class UnionFindSet(object):
    def __init__(self, n):
        # m, n = len(grid), len(grid[0])
        self.roots = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]
        self.count = n
        
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
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from heapq import *
        queue = []
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(queue, (d, i, j))

        ufs = UnionFindSet(n)
        while ufs.count > 1:
            d, i, j = heappop(queue)

            if ufs.find(i) != ufs.find(j):
                res += d
                ufs.union(i, j)

        return res