class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([char*freq for char,freq in collections.Counter(s).most_common()])