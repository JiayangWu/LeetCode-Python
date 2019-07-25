class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right = 0, 0
        interval_sum = nums[0]
        res = 1 << 31
        while right < len(nums) and left <= right:
            # print nums[left:right + 1], interval_sum, left, right
            if interval_sum < s:
                right += 1 #需要更多的数，向右拓展
                if right < len(nums):
                    interval_sum += nums[right]
            else:
                res = min(res, right - left + 1)                
                interval_sum -= nums[left]
                left += 1 #满足条件，试着缩小区间
        # res = min(res, right - left + 1)
        return res if res != 1 <<31 else 0
        