class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # dp[i][j] represents A[:i + 1], B[:j + 1] longest common subarray length
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        res = 0

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    res = max(dp[i][j], res)
        # print dp
        return res