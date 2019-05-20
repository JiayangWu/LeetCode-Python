class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A) + 1)]
        kcnt = [0 for i in range(K)]
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
   
        return sum(x * (x - 1) // 2 for x in kcnt)
                