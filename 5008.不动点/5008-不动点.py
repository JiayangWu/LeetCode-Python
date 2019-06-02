class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i, x in enumerate(A):
            if i == x:
                return i
        return -1
            