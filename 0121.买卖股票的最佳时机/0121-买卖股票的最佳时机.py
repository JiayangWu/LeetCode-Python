class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if not prices:
        #     return 0
        minelement = 2 << 31
        profit = 0
        for i in range(len(prices)):
            minelement = min(minelement, prices[i])
            profit = max(profit, prices[i] - minelement)
        return profit