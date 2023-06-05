from heapq import *
from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        t = len(arr) // 2
        dic = Counter(arr)
        
        queue = []
        for key, val in dic.items():
            heappush(queue, -val)
        
        cnt = 0
        res = 0
        while cnt < t:
            tmp = heappop(queue)
            res += 1
            cnt += -tmp
            # print cnt, tmp, t
        return res