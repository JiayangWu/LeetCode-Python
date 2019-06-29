class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) < 2:
            return -1
        tmp = []
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                tmp.append(A[i] + A[j])
                
        tmp.sort()
        if tmp[0] > K:
            return -1
        # print tmp
        res = tmp[0]
        for item in tmp:
            if item < K and abs(item - K) < abs(res - K):
                res = item
        return res