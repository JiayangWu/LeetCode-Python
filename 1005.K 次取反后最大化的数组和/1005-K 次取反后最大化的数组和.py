class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cnt = 0
        for i in A:
            if i < 0:
                cnt += 1
                
        if cnt >= K:
            A.sort()
            s = -1 * sum(A[:K]) + sum(A[K:])
            return s
        
        else:
            temp = K - cnt
            B = list()
            
            for item in A:
                B.append(abs(item))
            # print B   
            B.sort()
            # print sum(B), B
            if temp % 2 == 1:
                return sum(B) - 2* B[0]
            else:
                return sum(B)
                   