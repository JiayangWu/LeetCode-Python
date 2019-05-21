class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return None
        m = len(nums)
        n = m
        self.dp = [0 for _ in range(m)]
        
        self.dp[0] = nums[0]
        
        for i in range(1, m):
            self.dp[i] = self.dp[i - 1] + nums[i]
        
        # print self.dp
        
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)