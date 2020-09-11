class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        s = set(arr)
        for i in range(1, max(arr) + k + 1):
            if i not in s:
                cnt += 1
            if cnt == k:
                return i