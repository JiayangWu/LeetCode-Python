class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pre = None
        for i, num in enumerate(nums):
            if num == 1:
                if pre != None:
                    if i - pre - 1 < k:
                        return False
                pre = i
        return True