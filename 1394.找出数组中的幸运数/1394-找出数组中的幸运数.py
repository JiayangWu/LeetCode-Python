class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = [key for key, val in collections.Counter(arr).items() if key == val]
        return max(l) if l else -1