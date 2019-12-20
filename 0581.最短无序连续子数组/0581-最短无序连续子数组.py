class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        if s == nums:
            return 0
        for i in range(len(s)):
            if s[i] != nums[i]:
                break
        for j in range(len(s) - 1, -1, -1):
            if s[j] != nums[j]:
                break
        # print i, j
        # print s, nums
        return len(s) - i - (len(s) - 1 -j)
                