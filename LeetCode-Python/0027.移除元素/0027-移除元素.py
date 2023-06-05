class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, right = 0, len(nums) - 1
        while i <= right:
            if nums[i] == val:
                while i < right and nums[right] == val:
                    right -= 1
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            i += 1
        return right + 1