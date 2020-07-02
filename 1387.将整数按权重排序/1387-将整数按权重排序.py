class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        dic = {}
        dic[1] = 0
        def func(x):
            if x in dic:
                return dic[x]
            if x % 2:
                res = 1 + func(3 * x + 1)
            else:
                res = 1 + func(x / 2)
            dic[x] = res
            return res

        return sorted(range(lo, hi + 1), key = lambda x: (func(x), x))[k - 1]