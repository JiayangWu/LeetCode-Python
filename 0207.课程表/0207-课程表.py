class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        if not prerequisites: #没有前置课的要求
            return True
        
        indegree = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        
        for end, start in prerequisites:
            indegree[end] += 1
            adj[start].add(end)
        
        queue = deque()
        for i, x in enumerate(indegree):
            if not x: #入度为0的结点入队
                queue.append(i)
        
        cnt = 0
        while queue:
            cur = queue.popleft()
            cnt += 1 #当前的cur满足条件
            
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)
    
        return cnt == numCourses
                    