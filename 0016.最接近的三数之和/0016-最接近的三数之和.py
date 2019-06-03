class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 99999999
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while(left < right):
                s = num + nums[left] + nums[right]
                
                if abs(s - target) < abs(res - target):
                    res = s
                
                if s == target:
                    return s
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return res