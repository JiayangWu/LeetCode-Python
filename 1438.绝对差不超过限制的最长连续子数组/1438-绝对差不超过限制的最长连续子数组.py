class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0
        from heapq import *
        res = 1
        minHeap = []
        maxHeap = []
        pre = 0
        for i in range(0, len(nums)):
            heappush(minHeap, (nums[i], i))
            heappush(maxHeap, (-nums[i], i))
            while -minHeap[0][0] - maxHeap[0][0]  > limit:
                while maxHeap and maxHeap[0][1] <= pre:
                    heappop(maxHeap)
                while minHeap and minHeap[0][1] <= pre:
                    heappop(minHeap)
                pre += 1
            res = max(res, i - pre + 1)
        return res