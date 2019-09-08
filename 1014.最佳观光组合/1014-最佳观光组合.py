class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        pre_max = A[0] + 0 #初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j) #判断能否刷新res
            pre_max = max(pre_max, A[j] + j) #判断能否刷新pre_max， 得到更大的A[i] + i
                
        return res