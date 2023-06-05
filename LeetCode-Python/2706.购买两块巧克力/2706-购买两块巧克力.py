class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s = prices[0] + prices[1]
        return money if s > money else money - s