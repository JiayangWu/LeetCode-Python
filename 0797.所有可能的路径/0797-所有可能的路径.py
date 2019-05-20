class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = list()
        n = len(graph)
        def dfs(start, tmp):
            if graph[start] == [] and start == n - 1:#没有下一个节点
                tmp += graph[start]
                res.append(tmp[:])
                return
            
            l = graph[start]
            for node in l:
                tmp.append(node)
                dfs(node, tmp)
                tmp.pop()

        dfs(0, [0])        
        return res