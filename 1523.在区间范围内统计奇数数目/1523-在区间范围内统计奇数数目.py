class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 + high % 2 == 0:
                return (high - low) // 2
        return 1 + (high - low) // 2