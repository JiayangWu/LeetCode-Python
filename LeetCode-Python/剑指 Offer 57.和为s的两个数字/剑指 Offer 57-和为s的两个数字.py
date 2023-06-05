class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target - num:
                    return [num, target - num]
                elif nums[mid] < target - num:
                    left = mid + 1
                else:
                    right = mid - 1