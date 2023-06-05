class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [price for price in prices]
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                last_index = stack[-1]
                res[last_index] = res[last_index] - price
                stack.pop()
            stack.append(i)
        return res