class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        from heapq import *
        if not tasks:
            return []

        tasks = [(pair[1], index, pair[0]) for index, pair in enumerate(tasks)] # 打包原始下标
        tasks.sort(key = lambda x: x[2]) # 按入队时间排序

        next_task_id = 0 # 下一项要干的工作
        cur_time = tasks[0][2]
        min_heap = []
        res = []
        while next_task_id < len(tasks) or min_heap:
            while next_task_id < len(tasks) and tasks[next_task_id][2] <= cur_time:
                # 入队所有已经可以开始干的工作
                heappush(min_heap, tasks[next_task_id])
                next_task_id += 1

            # 开始工作
            if not min_heap:
                # 直接跳到下一个有效时间
                cur_time = tasks[next_task_id][2]
            else:
                # 工作
                working_task = heappop(min_heap)
                cur_time += working_task[0]
                res.append(working_task[1])

        return res