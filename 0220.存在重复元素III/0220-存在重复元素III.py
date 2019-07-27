class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        record = []
        for i, num in enumerate(nums):
            record.append([num, i])
        record.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if record[j][0] - record[i][0] > t:
                    break
                if abs(record[i][1] - record[j][1]) <= k:
                    return True
        return False