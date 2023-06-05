class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 1. find the right-most negative number
        negative_index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                negative_index = mid
                left = mid + 1
            elif nums[mid] >= 0:
                right = mid - 1
        
        # print(negative_index)
        # 2. find the left-most positive number
        positive_index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                positive_index = mid
                right = mid - 1
            else:
                left = mid + 1

        if negative_index > -1 and positive_index > -1:
            return max(negative_index + 1, len(nums) - positive_index)
        elif negative_index > -1:
            return negative_index + 1
        elif positive_index > -1:
            return len(nums) - positive_index
        return 0