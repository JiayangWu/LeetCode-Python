class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        dp = triangle[:]
        for i in range(1, len(dp)):
            dp[i][0] += dp[i - 1][0]
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
            dp[i][-1] += dp[i - 1][-1]
            
        return min(dp[-1]) 