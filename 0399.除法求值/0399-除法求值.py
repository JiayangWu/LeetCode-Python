class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        
        #½¨Í¼
        for idx, equa in enumerate(equations):
            start, end = equa[0], equa[1]
            graph[start].add(end)
            graph[end].add(start)
            weight[(start, end)] = values[idx]
            weight[(end, start)] = 1.0 / values[idx]
            
        def dfs(start, end, visited):
            if (start, end) in weight:
                return weight[(start, end)]
            
            if start not in graph or end not in graph:
                return 0
            
            if start in visited:
                return 0
            
            visited.add(start)
            tmpres = 0
            for tmp in graph[start]:
                res = weight[(start, tmp)] * dfs(tmp, end, visited)
                if res != 0:
                    weight[(start, end)] = res
                    break
                    
            visited.remove(start)
            return res
            
        
         
        res = []
        for que in queries:
            start, end = que[0], que[1]
            tmp = dfs(start, end, set())
            if tmp == 0:
                tmp = - 1.0
            res.append(tmp)
                
        return res