class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        dp = [0 for _ in range(len(prob) + 1)]
        dp[1] = prob[0]
        dp[0] = 1 - prob[0]
        for i in range(1, len(prob)):
            new_dp = [0 for _ in range(len(prob) + 1)]
            for j in range(target + 1):
                new_dp[j] = dp[j] * (1 - prob[i]) + dp[j - 1] * prob[i]
            dp = new_dp[:]
        return dp[target]
    
        # dp = [[0 for _ in range(len(prob) + 1)] for _ in range(len(prob))]
        # # dp[i][j] 表示前i个硬币里，有j个硬币正面朝上的概率
        # dp[0][1] = prob[0]
        # dp[0][0] = 1 - prob[0]
        # for i, p in enumerate(prob):
        #     for j in range(target + 1):
        #         if i > 0:
        #             dp[i][j] += dp[i - 1][j] * (1 - p)
        #             dp[i][j] += dp[i - 1][j - 1] * (p)
        # return dp[-1][target]