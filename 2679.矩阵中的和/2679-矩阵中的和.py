from heapq import *
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # if not nums or not nums[0]:
        #     return 0
        # m, n = len(nums), len(nums[0])
        # all_max_heap = []
        # for num in nums:
        #     max_heap = [-n for n in num]
        #     heapify(max_heap)
        #     all_max_heap.append(max_heap)

        # res = 0
        # for _ in range(n):
        #     score = 0
        #     for i in range(m):
        #         score = max(score, -heappop(all_max_heap[i]))
        #     res += score
        # return res
        for num in nums:
            num.sort()

        return sum(max(col) for col in zip(*nums))