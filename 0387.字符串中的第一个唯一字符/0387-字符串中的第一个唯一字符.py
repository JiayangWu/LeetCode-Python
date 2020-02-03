class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        
        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i
        return -1