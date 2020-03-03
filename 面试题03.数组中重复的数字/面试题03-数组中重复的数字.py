class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)