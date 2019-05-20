class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0 for _ in range(len(A))]
        
        for i, x in enumerate(A): #扫描每个数
            subarray_max = x
            for j in range(1, K + 1): # J 代表当前子数组的长度，包括A[i], 子数组是A[i - (j - 1): i + 1]
                if i - (j - 1) >= 0:#首先至少能向前构成这长度为 J 的子数组，
                    subarray_max = max(subarray_max, A[i - (j - 1)]) #确保subarray_max是从子数组的最大值
                    #这么写subarray_max = max(A[i - (j - 1): i + 1]]也可以过，但是很慢
                    
                    if i - j < 0:  # A[i]之前恰好有j - 1个元素，而它们一共组成了长度为J的子数组，相当于当前子数组可以表示为A[:j]
                        dp[i] = max(dp[i], subarray_max * j)
                    else:
                        dp[i] = max(dp[i], dp[i - j] + subarray_max * j)

        return dp[-1]