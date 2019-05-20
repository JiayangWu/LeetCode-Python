class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        l = len(cost)

        dp = [0 for _ in range(l + 1)]
        
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, l):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return min(dp[l - 1], dp[l - 2]) 