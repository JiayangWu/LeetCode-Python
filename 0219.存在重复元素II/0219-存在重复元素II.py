class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic:
                if i - dic[num] <= k:
                    return True
            dic[num] = i
        return False