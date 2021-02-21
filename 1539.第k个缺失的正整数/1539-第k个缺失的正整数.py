class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr = set(arr)
        num = 1
        while k:
            if num not in arr:
                k -= 1

            num += 1
        return num - 1