class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        backup = nums[:]
        cnt = 0
        for i in range(1, len(nums), 2):
            if i != len(nums) - 1:
                if nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]:
                    nums[i] = (min(nums[i - 1], nums[i + 1]) - 1)
            else:
                if nums[i] >= nums[i - 1]:
                    nums[i] = (nums[i - 1] - 1)

        cnt = sum(backup) - sum(nums)
        nums = backup[:]
        cnt1 = 0
        for i in range(0, len(nums), 2):
            if i != 0 and i != len(nums) - 1:
                if nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]:
                    nums[i] = (min(nums[i - 1], nums[i + 1]) - 1)
            elif i == 0:
                if nums[i] >= nums[i + 1]:
                    nums[i] = (nums[i + 1] - 1)    
            elif i == len(nums) - 1:
                if nums[i] >= nums[i - 1]:
                    nums[i] = (nums[i - 1] - 1)    
        cnt1 = sum(backup) - sum(nums)
        return min(cnt, cnt1)