class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        dic = {}
        self.res = True
        
        def dfs(node):
            if not self.res:
                return
            
            for child in graph[node]:
                # print node, child
                if child in dic:
                    if dic[child] == dic[node]:
                        # print child, node, graph, dic
                        self.res = False
                        return
                else:
                    dic[child] = not dic[node]
                    dfs(child)
                    
        for node in range(len(graph)):
            if node not in dic:
                dic[node] = True
                dfs(node)
        return self.res
            