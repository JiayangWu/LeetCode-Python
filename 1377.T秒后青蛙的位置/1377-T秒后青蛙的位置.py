class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        from collections import deque, defaultdict
        
        # 1. 建图
        adj = defaultdict(set)
        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)
        
        # 2. 初始化 DP 数组
        # dp[k][node] 代表在第 k 秒，蛤处于 node 的概率
        # dp[k][node] += dp[k - 1][parent] * prbability(parent -> node)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(t + 1)]
        dp[0][1] = 1
        
        for time in range(1, t + 1):
            for par in range(1, n + 1):
                if dp[time - 1][par]:
                    if not adj[par]:
                        # 如果无处可去，则停留在原地
                        dp[time][par] = dp[time - 1][par]
                    else:
                        # 能跳就跳
                        for node in adj[par]:
                            dp[time][node] += dp[time - 1][par] * 1.0 / len(adj[par])
                            
                        # 跳完就把用过的边删掉
                        for node in adj[par]:
                            adj[node].remove(par)
                        adj[par] = set()

        return dp[t][target]
        