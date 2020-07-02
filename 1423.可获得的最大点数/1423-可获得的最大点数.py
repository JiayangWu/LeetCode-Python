class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # 连续摸 n - k 张牌，求最小点数和
        n = len(cardPoints)
        s = sum(cardPoints)

        left, right = 0, n - k
        window_sum = sum(cardPoints[left:right])
        min_s = window_sum
        for right in range(n - k, n):
            # print cardPoints[left:right + 1]
            window_sum -= cardPoints[left]
            window_sum += cardPoints[right]
            min_s = min(min_s, window_sum)
            left += 1
        return s - min_s
