class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        g = nums[0]
        for num in nums:
            g = gcd(g, num)
        return g == 1