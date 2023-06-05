class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = None
        res = 0
        for price in prices:
            if prev_min is None or prev_min > price:
                prev_min = price
            res = max(res, price - prev_min)
        return res