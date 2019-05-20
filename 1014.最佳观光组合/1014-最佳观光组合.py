class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        mmax = A[0]
        mmax_index = 0
        for j in range(1, len(A)):
            res = max(res, mmax + A[j] + mmax_index - j)
            if A[j] + j > mmax + mmax_index:
                mmax = A[j]
                mmax_index = j
                
        return res