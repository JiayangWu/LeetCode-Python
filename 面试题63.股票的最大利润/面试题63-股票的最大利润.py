class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        pre_min = prices[0] if prices else 0
        for price in prices:
            res = max(res, price - pre_min)
            pre_min = min(pre_min, price)
        return res