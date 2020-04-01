class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # from collections import defaultdict
        target = sum(A) // 3
        snow = 0
        cnt = 0
        for i, x in enumerate(A):
            snow += x
            if target == snow:
                snow = 0
                cnt += 1
        return cnt >= 3
