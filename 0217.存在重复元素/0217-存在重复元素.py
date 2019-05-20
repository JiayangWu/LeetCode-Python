class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = dict()
        for num in nums:
            if record.get(num, 0):
                return True
            record[num] = 1
        return False

                
        