class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        indegree = defaultdict(int)
        children = defaultdict(set)
        all_courses = set()
        for cur, pre in prerequisites:
            indegree[cur] += 1
            children[pre].add(cur)
            all_courses.add(cur)
            all_courses.add(pre)

        queue = deque([])
        for course in all_courses:
            if indegree[course] == 0:
                queue.append(course)
        # 2. BFS, let course with indegree 0 leave a queue, and let its children with indegree 0 into the queue
        res = []

        while queue:
            cur = queue.popleft()

            res.append(cur)
            for child in children[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(res) != len(all_courses):
            return []
        for course in range(numCourses):
            if course not in all_courses:
                res.append(course)
        return res