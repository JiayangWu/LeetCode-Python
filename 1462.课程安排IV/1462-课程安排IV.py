class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        from collections import defaultdict
        from heapq import *
        pre = defaultdict(set)
        children = defaultdict(set)            
        inDegree = defaultdict(int)
            
        for src, dec in prerequisites:
            inDegree[dec] += 1
            children[src].add(dec)

        queue = []
        for i in range(n):
            if inDegree[i] == 0:
                heappush(queue, i)
                
        while queue:
            cur = heappop(queue)

            for child in children[cur]:
                pre[child] = pre[cur] | set([cur]) | pre[child]
                
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    heappush(queue, child)

        res = []
        for src, dec in queries:
            res.append(src in pre[dec])
        return res