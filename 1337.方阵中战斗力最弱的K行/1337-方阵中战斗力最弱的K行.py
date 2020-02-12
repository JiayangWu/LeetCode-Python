class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        res = []
        for i, row in enumerate(mat):
            res.append((sum(row), i))
            
        return [i for s, i in sorted(res)[:k]]