class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        res = [(x, i) for i, x in enumerate(arr)]
            
        res.sort()
        # print res
        dp = [1 for _ in res]
        
        for k in range(len(arr)):
            i = res[k][1]
            for j in range(1, d + 1):
                if i + j == len(arr) or arr[i + j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[i + j] + 1)
            
            for j in range(1, d + 1):
                if i - j < 0 or arr[i - j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[i - j] + 1)
        return max(dp)