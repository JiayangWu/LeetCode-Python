class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        red_nei, blue_nei = defaultdict(set), defaultdict(set)
        
        for start, end in red_edges: #记录下所有的从红色路径可以到达的邻居节点
            red_nei[start].add(end)
        for start, end in blue_edges: #记录下所有的从蓝色路径可以到达的邻居节点
            blue_nei[start].add(end)
            
        visited = set()
        queue = deque()
        queue.append((0, -1)) # -1 无色， 0 红色， 1蓝色
        distance = 0
        res = [-1] * n
        while queue:
            next_queue = deque()
            for cur, color in queue:
                if res[cur] == -1: #BFS保障了第一次到达终点时的距离一定是最短距离
                    res[cur] = distance
                if color == -1 or color == 0: #当前是红色，下一次在蓝色里找
                    for nei in blue_nei[cur]:
                        if (cur, nei, 1) not in visited:
                            visited.add((cur, nei, 1))
                            next_queue.append((nei, 1))
                if color == -1 or color == 1: #当前是蓝色，下一次在红色里找
                    for nei in red_nei[cur]:
                        if (cur, nei, 0) not in visited:
                            visited.add((cur, nei, 0))
                            next_queue.append((nei, 0))
            queue = next_queue
            distance += 1
        return res
        