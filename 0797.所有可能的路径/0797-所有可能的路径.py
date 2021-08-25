class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        res = []
        def dfs(cur, path):
            path.append(cur)
            if cur == n - 1:
                res.append(path[:])
                return

            for nxt in graph[cur]:
                dfs(nxt, path[:])

        dfs(0, [])
        return res