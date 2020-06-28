class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                l.append(i)
        total = len(l) * 2 if l[-1] ** 2 != n else len(l) * 2 - 1
        if total < k:
            return -1
        
        if k - 1 < len(l):
            return l[k - 1]
        else:
            idx = (len(l) - 1) * 2 - k
            return n // l[idx] if total % 2 else n // l[idx + 2]
        