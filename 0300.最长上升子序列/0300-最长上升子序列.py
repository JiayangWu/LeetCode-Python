class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return 0
        dp = [1 for _ in range(l)]
        
        for index, item in enumerate(nums):
            dp[index] = self.find(nums[:index + 1], dp) + 1
        # print dp       
        return max(dp)
            
    
    def find(self, nums, dp):
        max_element = -1 * 2 << 31
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[-1]:
                max_element = max(max_element, dp[i]) 

        return max_element if max_element != -1 * 2 << 31 else 0