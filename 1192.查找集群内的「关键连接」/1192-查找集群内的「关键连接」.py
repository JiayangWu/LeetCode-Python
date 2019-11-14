from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = set()
        low = [9999999] * n
        discover = [999999] * n
        parent = [-1] * n
 
        graph = defaultdict(list)
        self.time = 0
        res = []
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u):
            visited.add(u)
            discover[u] = self.time
            low[u] = self.time
            self.time += 1
 
            for v in graph[u]:
                if v not in visited:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
 
                    if low[v] > discover[u]:
                        res.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], discover[v])
                
        for i in range(n):
            if i not in visited:
                dfs(i)
        return res
