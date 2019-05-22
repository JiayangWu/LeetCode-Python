class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        half_l = len(A) / 2
        temp = sorted(A)
        return temp[half_l] if temp[half_l] == temp[half_l + 1] else temp[half_l - 1]
        