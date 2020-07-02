class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        from heapq import *
        dic = Counter(nums)
        queue = []
        for digit, fre in dic.items():
            if len(queue) < k:
                heappush(queue, (fre, digit))
            else:
                heappushpop(queue, (fre, digit))
        # print queue
        res = []
        while queue:
            res.append(heappop(queue)[1])
        return res