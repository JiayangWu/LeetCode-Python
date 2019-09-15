class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if max(arr) < 0:
            return 0
        if sum(arr) > 0:
            res = sum(arr) * (k - 2)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            for i in range(1,len(arr)):
                dp[i] = dp[i - 1] + arr[i]
                    
            res += max(dp)
            dp = [0] * len(arr)
            dp[-1] = arr[-1]
            for i in range(len(arr) - 2, -1, -1):
                dp[i] = dp[i + 1] + arr[i]
                    
            res += max(dp)
            return (res)% (10 ** 9 + 7)
        
        arr = arr + arr
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1,len(arr)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + arr[i]
            else:
                dp[i] = arr[i]
                
        return max(dp) % (10 ** 9 + 7)
        