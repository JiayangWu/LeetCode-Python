class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for num in arr:
            mod = num % k
            if mod:
                dic[mod] += 1
        for key in dic.keys():
            if key * 2 != k and dic[key] != dic[k - key]:
                return False
            if key * 2 == k and dic[key] % 2 != 0:
                return False
        return True
             