class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. find all node/course with indegree 0, let them enter a queue
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
        studied_course = 0
        while queue:
            cur = queue.popleft()

            studied_course += 1
            for child in children[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return studied_course == len(all_courses)