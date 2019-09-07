class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                fast = 0
                while nums[slow] != nums[fast]:
                    slow = nums[slow]
                    fast = nums[fast]
                return nums[fast]