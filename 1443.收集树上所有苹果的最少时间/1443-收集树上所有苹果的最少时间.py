class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(set)
        mustVisitNodes = set()
        
        for src, des in edges:
            dic[src].add(des)
            dic[des].add(src)
            
        def findMustVisitNodesDFS(node, path, visited):
            path.append(node)
            
            if hasApple[node]:
                for n in path:
                    mustVisitNodes.add(n)
            
            for child in dic[node]:
                if child not in visited:
                    visited.add(child)
                    findMustVisitNodesDFS(child, path + [node], visited)
                
        findMustVisitNodesDFS(0, [], set([0]))

        return max(0, 2 * (len(mustVisitNodes) - 1))