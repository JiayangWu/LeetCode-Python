class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import * 
        
        queue = []
        for num in arr:
            if len(queue) < k:
                heappush(queue, -num)
            else:
                if queue and queue[0] < num:
                    heappush(queue, -num)
                    heappop(queue)
        return [-item for item in queue]