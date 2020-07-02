class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i, ans = 0, 0
        for a in sorted(A):
            ans += max(i - a, 0)
            i = max(a, i) + 1
        return ans