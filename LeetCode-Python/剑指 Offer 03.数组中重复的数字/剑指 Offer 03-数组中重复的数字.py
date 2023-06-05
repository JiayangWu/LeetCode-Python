class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num != i:
                if nums[num] == num:
                    return num 
                nums[i], nums[num] = nums[num], nums[i]
        return nums[-1]