class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A == sorted(A) or A == sorted(A, reverse = True)