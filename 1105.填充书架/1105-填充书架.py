class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        dp = [999999999 for _ in range(len(books) + 1)]
        dp[0] = 0
        for i in range(1, len(books) + 1):
            w, h = 0, 0
            for j in range(i - 1, -1, -1):
                w += books[j][0]
                if w > shelf_width:
                    break
                h = max(h, books[j][1])
                dp[i] = min(dp[i], dp[j] + h)
        return dp[-1]