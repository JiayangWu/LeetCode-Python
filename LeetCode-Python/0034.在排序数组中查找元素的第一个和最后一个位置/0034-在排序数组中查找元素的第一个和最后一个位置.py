class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1. find the left-most index
        left, right = 0, len(nums) - 1
        left_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                left_index = mid
                right = mid - 1
            else:
                left = mid + 1
        print(left, right, left_index)
        # 2. find the right-most index
        left, right = 0, len(nums) - 1
        right_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                right_index = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return [left_index, right_index] if left_index > -1 and nums[left_index] == target else [-1, -1]