class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        return sorted(arr, key = lambda x: abs(x - m))[-k:]