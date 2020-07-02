class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow, fast = 0, 0
        while 1:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                fast = 0
                while nums[fast] != nums[slow]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]
