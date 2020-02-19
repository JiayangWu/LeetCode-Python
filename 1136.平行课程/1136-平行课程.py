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
            indegree[cur] += 1 #统计入度
            adj[pre].add(cur) #统计邻居节点
            
        from collections import deque
        queue = deque()
        for i, x in enumerate(indegree):
            if x == 0 and i > 0: #将入度为0的节点入队
                queue.append(i)

        semester_cnt= 0
        finished_course = 0
        while queue:
            next_queue = deque()
            semester_cnt += 1 #新的学期来了
            for cur in queue:         
                finished_course += 1 #又一门课学完了
                for neighbor in adj[cur]:
                    indegree[neighbor] -= 1
 
                    if indegree[neighbor] == 0:
                        next_queue.append(neighbor) #下个学期可以学neighbor这门课了
            queue = next_queue
        return semester_cnt if finished_course == N else -1 #如果所有的课都学完了，那么finished_course == N