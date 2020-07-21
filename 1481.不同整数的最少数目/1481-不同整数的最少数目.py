class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if not arr or len(arr) == k:
            return 0
        from collections import Counter
        dic = Counter(arr)
        l = dic.values()
        l = sorted(l)[::-1]
        
        target = len(arr) - k
        s = 0
        for i, num in enumerate(l):
            s += num
            if s >= target:
                return i + 1
        