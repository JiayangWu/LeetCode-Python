class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        for i in range(len(prices) - 1, -1, -1):
            if not stack:
                res.append(prices[i])
            else:
                while stack and stack[-1] > prices[i]:
                        stack.pop()
                if stack:
                    res.append(prices[i] - stack[-1])
                else:
                    res.append(prices[i])
            stack.append(prices[i])
        return res[::-1]