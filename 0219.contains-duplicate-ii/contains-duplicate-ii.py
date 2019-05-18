class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = dict()
        for i, num in enumerate(nums):
            # print record
            if record.get(num, -1) != -1:
                if i - record[num] <= k:
                    return True
            record[num] = i
        return False
                