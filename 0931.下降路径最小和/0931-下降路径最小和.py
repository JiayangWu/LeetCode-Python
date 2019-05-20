class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        m = len(A)
        n = m
        
        if A == [[]]:
            return 0
        
        dp = [[0 for _ in range(n)] for t in range(m)]
        for i in range(n):
            dp[0][i] = A[0][i]
            
        for i in range(1, m):
            for j in range(n):
                if not j: # the first column 
                    # if j + 1 <= n - 1: # j + 1 column exists
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
                elif j == n - 1: # the last column
                    # if j - 1 >= 0: # j -1 column exists
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + A[i][j]
                else:
                    # if j + 1 < n - 1 and j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + A[i][j]
                # print dp
        return min(dp[-1])
                    
                    