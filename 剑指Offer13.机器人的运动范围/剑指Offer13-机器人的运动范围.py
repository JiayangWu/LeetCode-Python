class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def dis(x, y):
            res = 0
            while x:
                res += x%10
                x //= 10
            while y:
                res += y%10
                y //= 10
            return res            
        dp = [[False]*105 for _ in range(105)]
        dp[0][0] = True
        ans = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if ((i!=0 and dp[i-1][j]) or (j!=0 and dp[i][j-1])) and dis(i, j)<=k:
                    dp[i][j] = True
                    ans += 1        
        return ans     