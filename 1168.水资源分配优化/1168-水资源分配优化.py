
class UnionFindSet(object):
    def __init__(self, n):

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
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        from heapq import *
        for i, well in enumerate(wells):
            pipes.append([0, i + 1, well])
        
        queue = []
        ufs = UnionFindSet(n)
        for start, end, cost in pipes:
            queue.append([cost, start, end])
            
        heapify(queue)
        res = 0
        while ufs.count > 0:
            
            cost, start, end = heappop(queue)
            # print ufs.roots, cost, start, end
            if ufs.find(start) == ufs.find(end):
                continue
            res += cost
            ufs.union(end, start)
        return res
        
        