class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # G(i) = i ^ (i /2)
        dp = [0 for _  in range(2 ** n)]
        for i in range(1, 2 ** n):
            dp[i] = i ^ (i /2)
        return dp