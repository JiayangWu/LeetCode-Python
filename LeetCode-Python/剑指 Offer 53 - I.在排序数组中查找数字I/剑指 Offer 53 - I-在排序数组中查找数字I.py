class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.count(target)
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

        return right_index - left_index + 1 if left_index > -1 else 0