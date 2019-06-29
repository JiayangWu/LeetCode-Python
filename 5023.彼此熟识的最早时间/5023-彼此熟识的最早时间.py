class UnionFindSet(object):
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = 0

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
    
    def check(self):
        print self.roots
        flag = self.find(self.roots[0])
        for i in self.roots:
            if self.find(i) != flag:
                return False
        return True

class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs = sorted(logs, key = lambda x:x[0])
        ufs = UnionFindSet(N)
        for time, x, y in logs:
            ufs.union(x, y)
            if ufs.check():
                return time
        return -1