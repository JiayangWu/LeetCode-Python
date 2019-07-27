class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        indegree = [0 for i in range(N + 1)]
        adj = [set() for _ in range(N + 1)]
        for pre, cur in relations:
            indegree[cur] += 1
            adj[pre].add(cur)
            
        from collections import deque
        queue = deque()
        for i, x in enumerate(indegree):
            if x == 0 and i > 0:
                queue.append(i)
        print queue
        cnt, res = 0, 0
        out = 0
        while queue:
            next_queue = deque()
            cnt += 1
            for cur in queue:         
                out += 1
                for neighbor in adj[cur]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        next_queue.append(neighbor)
            queue = next_queue
        return cnt if out == N else -1
        
            
            