class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key = lambda x:(str(bin(x)).count("1"), x))