class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        res = set()
        for i in range(k + 1):
            res.add(shorter * i + longer * (k - i))
        return sorted(list(res)) if k else []