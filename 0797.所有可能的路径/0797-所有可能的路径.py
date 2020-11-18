class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        visited = set()
        def dfs(cur_node, path):
            if cur_node == n - 1:
                res.append(path[:])
                return
            for next_node in graph[cur_node]:
                dfs(next_node, path + [next_node])
        res = []
        dfs(0, [0])
        return res