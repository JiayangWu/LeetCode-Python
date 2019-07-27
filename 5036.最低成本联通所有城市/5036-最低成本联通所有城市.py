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
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type conections: List[List[int]]
        :rtype: int
        """
        from collections import deque
        from heapq import *
        ufs = UnionFindSet(N)
        queue = []
        
        for start, end, cost in connections:
            ufs.union(start, end)
            queue.append([cost, start, end])
            
        if ufs.count != 1:
            return -1 #无法连接在一起
        #到这里可以保证一定可以把所有城市连在一起
        ufs2 = UnionFindSet(N)
        heapify(queue)       
        res = 0
        while ufs2.count > 1:
            cost, start, end = heappop(queue)
            if ufs2.find(start) == ufs2.find(end):
                continue
            ufs2.union(start, end)
            res += cost
        return res
            
        