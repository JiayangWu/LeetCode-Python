class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from collections import defaultdict
        from heapq import *
        num2idx = defaultdict(list)
        for i, num in enumerate(nums1):
            num2idx[num] = [i]

        for i, num in enumerate(nums2):
            num2idx[num].append(i)

        dups = set() 
        for key, val in num2idx.items():
            if len(val) > 1:
                dups.add(key)

        num2sum = defaultdict(int)
        res = 0
        queue = [(-nums1[-1], len(nums1) - 1, 0, 1), (-nums2[-1], len(nums2) - 1, 0, 2)]
        heapify(queue)
        while queue:
            val, idx, s, flag = heappop(queue)
            val = -val

            if flag == 1 and idx + 1 < len(nums1) and nums1[idx + 1] in dups:
                s = max(num2sum[nums1[idx + 1]], s)
            elif flag == 2 and idx + 1 < len(nums2) and nums2[idx + 1] in dups:
                s = max(num2sum[nums2[idx + 1]], s)

            if val in dups:
                s = max(num2sum[val], s + val)
                num2sum[val] = max(s, num2sum[val])
            else:
                s += val 

            if idx:
                if flag == 1:
                    heappush(queue, (-nums1[idx - 1], idx - 1, s, 1))
                else:
                    heappush(queue, (-nums2[idx - 1], idx - 1, s, 2))
            res = max(res, s)
        return res % (10 ** 9 + 7)
        