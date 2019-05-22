class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        dp = costs
        
        def GetMin(idx, k):
            Min = max(costs[idx])
            for i, cost in enumerate(costs[idx]):
                if i == k:
                    continue
                Min = min(Min, cost)
            return Min
        
        for i in range(1, len(costs)):
            for k in range(len(costs[i])):
                dp[i][k] += GetMin(i - 1, k)
        return min(dp[-1])
            