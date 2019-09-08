class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #1. 二分找旋转点
        #2. 确认target落在哪一侧然后二分找
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        midposition = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print mid
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                midposition = mid
                break
            elif nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid - 1
        # print midposition       
        if midposition != -1:
            if target >= nums[0]:
                left, right = 0, midposition
            else:
                left, right = midposition + 1, len(nums) - 1
        else:
            left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1