class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        return  0 if A[-1] - A[0] - 2*K <= 0 else A[-1] - A[0] - 2*K     
        