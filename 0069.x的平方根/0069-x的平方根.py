class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            s = mid ** 2
            if s == x:
                return mid
            elif s < x:
                left = mid + 1
            elif s > x:
                right = mid - 1
        return left - 1