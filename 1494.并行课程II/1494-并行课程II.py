class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        children = defaultdict(set)
        
        for src, dec in dependencies: # 建图
            inDegree[dec] += 1
            outDegree[src] += 1
            children[src].add(dec)
            
        queue = []
        for i in range(1, n + 1):
            if inDegree[i] == 0: # 入度为0（没有先修课了）的课入队
                heappush(queue, (-outDegree[i], i, -1)) # 出度越大（以这门课作为先修课的课越多），优先级越高 
        
        semesterCnt = 0
        while queue:
            semesterCnt += 1
            nextSemesterCourses = [] # 存放这个学期不能上的课
            courseCnt = 0
            while courseCnt < k and queue: # 每个学期最多上 k 门课
                priority, node, preFinishedSemester = heappop(queue)

                if preFinishedSemester >= semesterCnt: # 当前学期不能上这门课
                    nextSemesterCourses.append((priority, node, preFinishedSemester))
                    continue
                    
                for child in children[node]: # 这门课可以学，学它，然后处理孩子课的入度
                    inDegree[child] -= 1
                    
                    if inDegree[child] == 0: # 孩子课的先修课全上完了
                        heappush(queue, (-outDegree[child], child, semesterCnt))
                courseCnt += 1
                
            for item in nextSemesterCourses: # 把之前存起来的本学期不能上的课再重新入队
                heappush(queue, item)

        return semesterCnt
                
                
                    