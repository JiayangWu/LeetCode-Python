class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        max_element = max(nums)
        if max_element < 0:
            return 1
        i = 1
        while i < max_element:
        # for i in range(1, max_element):
            if i not in nums:
                return i
            i += 1
        return max_element + 1