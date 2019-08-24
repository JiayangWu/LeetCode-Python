class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        nums.sort()
        for i, num in enumerate(nums):
            # 现在要在比i大的下标里，找能组合出target - num 的两个数的组合
            t = target - num
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] >= t:
                    right -= 1 #和太大了，尝试把和缩小
                elif nums[left] + nums[right] < t:
                    res += right - left #在这种情况下，left可以与【left + 1， right】间任意一个数组成一组答案
                    left += 1

        return res