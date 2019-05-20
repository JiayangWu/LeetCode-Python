class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        la, lb = len(A), len(B)
        
        dp = [[0 for i in range(lb + 1)] for j in range(la + 1)]
        for i in range(1, la + 1):
            for j in range(1, lb + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print dp            
        return dp[-1][-1]
                        
        
        