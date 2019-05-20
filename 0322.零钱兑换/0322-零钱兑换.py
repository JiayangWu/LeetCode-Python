class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = list()
        max_int = 2 << 31
        
        for i in range(amount + 1):
            if i not in coins:
                dp.append(max_int)
            else:
                dp.append(1)
        
        for i in range(amount + 1):
            if i not in coins:
                for j in coins:
                    if i - j > 0:
                        dp[i] = min(dp[i - j] + 1, dp[i])
            
        return dp[amount] if dp[amount] != max_int else -1
        