class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = collections.Counter(arr)
        return len(d.values()) == len(set(d.values()))