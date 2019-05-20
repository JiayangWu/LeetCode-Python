class Solution(object):
    def longestOnes(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = len(A)
        zero = 0
        lo,hi = 0,0
        res = 0
        for hi in range(l):
            if A[hi] == 0:
                zero += 1
            while zero > k:               
                if A[lo] == 0:
                    zero -= 1
                lo += 1
            # print lo, hi
            res = max(res, hi - lo + 1)
            
        return res