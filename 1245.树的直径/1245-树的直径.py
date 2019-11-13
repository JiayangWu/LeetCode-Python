from collections import defaultdict        
class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0

        self.neibors = defaultdict(set)
        self.res = 0
        
        for start, end in edges: # 建树
            self.neibors[start].add(end)
        
        def getHeight(node):
            res = []
            for neibor in self.neibors[node]:
                res.append(getHeight(neibor))
            
            while len(res) < 2: # 如果孩子少于两个，就给它补空的上去
                res.append(0)
                
            res = sorted(res)
            self.res = max(self.res, sum(res[-2:])) # 取最长的两个子树长度
            return 1 + max(res)
        
        getHeight(edges[0][0])
        return self.res

        