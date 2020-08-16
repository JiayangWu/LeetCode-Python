class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        from collections import defaultdict
        par2child = defaultdict(set)
        for s, d in edges:
            par2child[d].add(s)
            par2child[s].add(d)

        self.res = [0 for _ in labels]
        def dfs(node, visited):
            dic = defaultdict(int)
            for child in par2child[node]:
                if child not in visited:
                    visited.add(child)
                    child_dic = dfs(child, visited)
                    for key, val in child_dic.items():
                        dic[key] = dic[key] + val
            # print(node, dic)
            self.res[node] = 1 + dic[labels[node]]
            dic[labels[node]] += 1
            return dic
        dfs(0, set([0]))
        return self.res

