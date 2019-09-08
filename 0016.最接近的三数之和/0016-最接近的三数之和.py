class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                s = num + nums[left] + nums[right]
                # print s, res, abs(s - target), abs(res - target)
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res
                
            
        