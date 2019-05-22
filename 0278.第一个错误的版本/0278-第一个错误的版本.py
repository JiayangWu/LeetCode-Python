
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while(end-start>1):
            mid = start + (end-start)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
            print start, end
        return start if isBadVersion(start) else end