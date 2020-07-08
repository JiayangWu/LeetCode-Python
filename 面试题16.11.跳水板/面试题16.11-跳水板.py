class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(k + 1):
            s = shorter * (k - i) + longer * i
            if not res or res[-1] != s:
                res.append(s)
        return res if k else []