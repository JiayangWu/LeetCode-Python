class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
        # print nums
        return max(nums) if n else 0