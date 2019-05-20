class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = list()
        for a in A:
            a.reverse()
            res.append((1 - i) for i in a)
        return res