class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        from heapq import *
        if not events:
            return 0
        # 排序并反转，反转是为了可以快速pop
        events = sorted(events, key = lambda x:(x[0], x[1]))[::-1]
        
        queue = []
        res = 0
        for day in range(1, 10 ** 5 + 1):
            # 把所有结束日期在当前日期之前的event都pop掉
            while queue and queue[0] < day:
                heappop(queue)
            
            # 把所有开始日期大于等于当前日期的event都push进队列
            while events and events[-1][0] <= day:
                last = events.pop()
                heappush(queue, last[1])
            
            if queue:
                # 如果当前日期有可以去的event，就去这一个
                heappop(queue)
                res += 1
            if not queue and not events:
                # 如果所有event都参加完了
                break
        
        return res