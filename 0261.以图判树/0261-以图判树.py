class UnionFindSet(object):
    def __init__(self, n):
        self.count = n
        self.roots = [i for i in range(n)]
        
    def find(self, node):
        while self.roots[node] != node:
            node = self.roots[node]
        return node
    
    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        self.roots[p_parent] = q_parent
        self.count -= 1
        
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        #开并查集，如果一条边的两个顶点在放进图之前就有相同的根结点，则说明这条边放进去之后会形成一个环
        ufs = UnionFindSet(n)
        for start, end in edges:
            if ufs.find(start) == ufs.find(end):
                return False
            ufs.union(start, end)
        # print ufs.count
        return ufs.count == 1