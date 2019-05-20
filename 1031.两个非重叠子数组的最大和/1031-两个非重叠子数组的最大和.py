class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        # hashmap[index] = sum来记录长度为L的子数组的和，以及下标
        lhash, mhash = dict(), dict()
        for i in range(len(A) - L + 1):
            if i == 0:
                lhash[i] = sum(A[:L])
            else:
                lhash[i] = lhash[i - 1] - A[i - 1] + A [i + L - 1]
                # if L > 1:
                
        for i in range(len(A) - M + 1):
            if i == 0:
                mhash[i] = sum(A[:M])
            else:
                mhash[i] = mhash[i - 1] - A[i - 1] + A [i + M - 1]      
        
        res = 0
        #L 在前， M 在后
        for i in range(0, len(A) - L + 1):
            if i > len(A) - M: #放不下M 了
                break
            for j in range(i + L - 1 + 1, len(A) - M + 1):
                # print i, j, lhash[i], mhash[j], res
                res = max(res, lhash[i] + mhash[j])
                
        #M 在前， L 在后
        for j in range(0, len(A) - M + 1):
            if j > len(A) - L: #放不下L 了
                break
            for i in range(j + M - 1 + 1, len(A) - L + 1):
                # print i, j, lhash[i], mhash[j]
                res = max(res, lhash[i] + mhash[j])
                
        return res
                                                     